import argparse
import sys
import os
import time
import tqdm


from cvplayer.player import VideoPlayer

parser = argparse.ArgumentParser(prog='cvplay')

parser.add_argument("filename",
                    default="",
                    type=str,
                    help="path to the video file to be played")

parser.add_argument("-p", "--paused",
                    action="store_true",
                    help="the player is in a paused state when initialized")

parser.add_argument("-f", "--fullscreen",
                    action="store_true",
                    help="the player is in fullscreen mode when initialized")

parser.add_argument("-i", "--skip-interval",
                    type=int,
                    metavar="",
                    default=5,
                    help="number of seconds to skp by when skipping ahead or behind")

parser.add_argument("-l", "--list",
                    action="store_true",
                    help="list all the playback keybinds")

args = parser.parse_args()

player = VideoPlayer(args.filename, args.paused, args.fullscreen, skip_interval=args.skip_interval)

print(f"\n::playing {os.path.split(args.filename)[1]}\n")

bar_format = '{elapsed} |' + '{bar}' + '| {remaining}'
with tqdm.tqdm(range(player.get_metadata()['duration']), unit='s', bar_format=bar_format) as bar:
    while player.state != 'eof':
        current_pts = player.get_pts()
        time.sleep(0.7)
        if player.state == 'paused':
            continue
        updated_pts = player.get_pts()
        if not isinstance(updated_pts, str):
            pts_diff = updated_pts - current_pts
        else:
            pts_diff = 1
        if pts_diff != 1:
            bar.update(pts_diff)
            bar.refresh()
            continue
        bar.update(1)
        bar.refresh()
        time.sleep(0.3)
    bar.update(1)
    sys.exit(0)
