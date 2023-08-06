#!/usr/bin/env python

import sys
import argparse

import qth
import asyncio

from qth_gc.version import __version__


async def get_all_topics(client, wait=3.0):
    """Gather a dictionary of all topic/message pairs received in response to a
    global subscription.
    """
    topics = {}
    changed = [True]
    
    def on_message(topic, payload):
        topics[topic] = payload
        changed[0] = True
    await client.subscribe("#", on_message)
    while changed[0]:
        await asyncio.sleep(wait)
        changed[0] = False
    await client.unsubscribe("#", on_message)
    return topics

def traverse_tree(topics, root=""):
    """Traverse the topic tree published by the Qth registrar, iterating over
    all of the registered topic names (including the topics used by the topic
    tree itself which are not actually listed in the tree themselves). The
    resulting set of topics will be complete but may contain duplicates.
    
    Parameters
    ----------
    topics : {topic: message}
    root : str
        Internal use. The part of the topic tree to traverse from.
    """
    # The directory tree which otherwise may not be listed
    listing = "meta/ls/{}".format(root)
    yield listing
    
    for topic, entries in topics[listing].items():
        is_directory = False
        is_non_directory = False
        for entry in entries:
            is_directory |= entry["behaviour"] == qth.DIRECTORY
            is_non_directory |= entry["behaviour"] != qth.DIRECTORY
        
        if is_non_directory:
            yield root + topic
        if is_directory:
            yield from traverse_tree(topics, "{}{}/".format(root, topic))


def find_garbage(topics):
    """Return an iterable of the orphaned/garbage topics found in the topic
    tree.
    """
    # All potential topics (ignoring any MQTT system ones)
    all_topics = set(t for t in topics if not t.startswith("$"))
    
    registered_topics = set(traverse_tree(topics))
    
    return all_topics - registered_topics


async def delete_garbage(client, garbage):
    """Delete all topics listed as garbage."""
    if garbage:
        done, pending = await asyncio.wait([asyncio.create_task(client.delete_property(topic))
                                            for topic in garbage])
        assert len(pending) == 0


def main(args=None):
    """Command-line launcher for the garbage collector.

    Parameters
    ----------
    args : [arg, ...]
        The command-line arguments passed to the program.
    """
    parser = argparse.ArgumentParser(
        description="Discovers retained MQTT messages for topics not listed by "
                    "the Qth registrar. Use the -d flag to delete these "
                    "messages.")
    parser.add_argument("--version", "-V", action="version",
                        version="%(prog)s {}".format(__version__))
    parser.add_argument("--host",
                        default=None,
                        help="The hostname of the MQTT broker.")
    parser.add_argument("--port",
                        default=None, type=int,
                        help="The port number for the MQTT broker.")
    parser.add_argument("--load-time",
                        default=3.0, type=float,
                        help="The number of seconds to wait for the "
                             "retained topics to stop arriving after "
                             "subscription.")
    parser.add_argument("--remove", "-r", action="store_true",
                        help="Remove the discovered garbage entries.")
    parser.add_argument("--force", "-f", action="store_true",
                        help="Don't ask for confirmation before deleting.")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Don't print a list of garbage topics.")
    args = parser.parse_args(args)
    
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    client = qth.Client("qth_gc", host=args.host, port=args.port)
    try:
        # Discover all garbage and print to the command line
        topics = loop.run_until_complete(get_all_topics(
            client, wait=args.load_time))
        garbage = find_garbage(topics)
        
        # Print the garbage
        if not args.quiet:
            for topic in sorted(garbage):
                print(topic)
        
        # Do nothing if no garbage present
        if len(garbage) == 0:
            if not args.quiet:
                sys.stderr.write("No garbage to delete.\n")
            return 0
        
        if not args.remove:
            # User didn't ask to remove entries so just leave it at listing
            # them
            sys.stderr.write(
                "WARNING: Not removing garbage topics (add -r for this)\n")
            return 0
        else:
            # Confirm deletion, if required
            if not args.force:
                sys.stderr.write("Delete these topics?\n  (y/N): ")
                sys.stderr.flush()
                choice = input()
                if choice.strip().lower() not in ("yes", "y"):
                    sys.stderr.write("Topics not deleted.\n")
                    return 1
            
            # Delete the entries
            loop.run_until_complete(delete_garbage(client, garbage))
            return 0
    finally:
        loop.run_until_complete(client.close())

    return 0


if __name__ == "__main__":  # pragma: no cover
    import sys
    sys.exit(main())
