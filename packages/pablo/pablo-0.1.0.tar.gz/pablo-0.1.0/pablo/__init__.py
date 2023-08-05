import essentia
essentia.log.warningActive = False

import os
import math
import click
import shutil
import random
from glob import glob
from colorama import Fore
from pablo import analysis, mutate, heuristics, producer, diglet
from pablo.models.sample import Slice
from pablo.models.song import Song


formats = ['mp3', 'wav', 'aif']


@click.group()
def cli():
    pass


def echo(tmp, *txts, **kwargs):
    color = kwargs.get('color', Fore.GREEN)
    txts = ['{0}{1}{2}'.format(color, txt, Fore.RESET) for txt in txts]
    print(tmp.format(*txts))


@cli.command()
@click.argument('library', type=click.Path(exists=True))
def analyze(library):
    """
    Analyze all songs in a directory

    Their analyses will be persisted to a local db.
    """
    files = []
    for fmt in formats:
        files += glob(os.path.join(library, '*.{0}'.format(fmt)))

    echo('Analyzing {0} songs...', len(files))
    with click.progressbar(files) as bar:
        for f in bar:
            analysis.analyze(f)


@cli.command()
@click.argument('song', type=click.Path(exists=True))
def analyze_song(song):
    """
    Analyze a single song
    """
    bpm, key = analysis.analyze(song)
    echo('\tBPM: {0}', bpm)
    echo('\tKey: {0} ({1})', key.key, key.scale)


@cli.command()
@click.argument('song', type=click.Path(exists=True))
@click.argument('library', type=click.Path(exists=True))
@click.option('-O', 'outdir', default=None, help='Copy the compatible songs to this directory', type=click.Path())
@click.option('--keyshift', is_flag=True, help='If -O has been set, this will key shift the copied songs as necessary')
def compatible(song, library, outdir, keyshift):
    """
    Returns mix-compatible songs for the given song in the given library
    """
    focal_bpm, focal_key = analysis.analyze(song)

    echo('Finding compatible songs for {0}', song, color=Fore.CYAN)
    echo('\tBPM: {0}', focal_bpm)
    echo('\tKey: {0} ({1})', focal_key.key, focal_key.scale)

    # Search for songs that require relatively small modifications
    # to match the focal song
    bpm_range_l = 0.85 * focal_bpm
    bpm_range_u = 1.15 * focal_bpm
    key_range = 3

    echo('Using library at {0}', library, color=Fore.CYAN)

    files = []
    for fmt in formats:
        files += glob(os.path.join(library, '*.{0}'.format(fmt)))

    echo('Working with {0} songs', len(files))

    # Select appropriate songs to mix
    echo('\n{0}', 'Compatible songs:', color=Fore.YELLOW)
    selections = []

    while files:
        song = files.pop()
        bpm, key = analysis.analyze(song)
        if bpm_range_l <= bpm <= bpm_range_u and (focal_key.mixable(key) or abs(focal_key.distance(key)) <= key_range):
            selections.append(song)
            echo('{0}', song, color=Fore.CYAN)

    if outdir is not None:
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        for song in selections:
            fname = os.path.basename(song)
            outfile = os.path.join(outdir, fname)

            if keyshift and not focal_key.mixable(key):
                bpm, key = analysis.analyze(song)
                mutate.key_shift(song, key, focal_key, outfile)
            else:
                shutil.copy(song, outfile)


@cli.command()
@click.argument('start', type=str)
@click.argument('outdir', type=click.Path(exists=True))
@click.option('-D', 'depth', default=2, help='How many levels of related vids to dig through', type=int)
@click.option('-T', 'max_duration', default=360, help='Only download videos below or equal to this duration', type=int)
def dig(start, outdir, depth, max_duration):
    echo('Digging from {0}', start, color=Fore.CYAN)
    diglet.dig(start, outdir, depth, max_duration)
    echo('{0}', 'Done digging')


@cli.command()
@click.argument('library', type=click.Path(exists=True))
@click.argument('outdir', type=click.Path())
@click.option('-F', 'focal', default=None, help='The song to base the mix around', type=click.Path(exists=True))
@click.option('-C', 'max_sample_size', default=32, help='The max sample size to generate samples with. Should be a power of 2', type=int)
@click.option('-c', 'min_sample_size', default=16, help='The min sample size to generate samples with. Should be a power of 2', type=int)
@click.option('-T', 'n_tracks', default=2, help='The number of tracks to produce and mix together', type=int)
@click.option('-S', 'n_songs', default=None, help='The number of songs to include (if enough are available)', type=int)
@click.option('-M', 'length', default=512, help='The length in beats for the song. Should be a power of 2', type=int)
@click.option('--debug', is_flag=True, help='If set, will debug with click track')
@click.option('--incoherent', is_flag=True, help='Make an "incoherent" mix (don\'t use markov chains)')
def mix(library, outdir, focal, max_sample_size, min_sample_size, n_tracks, n_songs, length, incoherent, debug):
    """
    Create a mix
    """
    if max_sample_size < min_sample_size:
        echo('{0}', 'The max sample size must be larger than the min sample size', color=Fore.RED)
        return

    n_u = math.log(max_sample_size, 2)
    if int(n_u) != n_u:
        echo('{0}', 'The max sample size must be a power of 2', color=Fore.RED)
        return

    n_l = math.log(min_sample_size, 2)
    if int(n_l) != n_l:
        echo('{0}', 'The min sample size must be a power of 2', color=Fore.RED)
        return

    dur = math.log(length, 2)
    if int(dur) != dur:
        echo('{0}', 'The song length must be a power of 2', color=Fore.RED)
        return

    if n_songs is not None and n_tracks > n_songs:
        echo('{0}', 'There must be at least as many songs as there are tracks', color=Fore.RED)
        return

    sample_sizes = [2**n for n in range(int(n_l), int(n_u) + 1)]

    # Prepare output directory, just to check if the directory is not empty
    outdir = os.path.join(outdir, 'pablo_mix')
    sample_dir = os.path.join(outdir, 'samples')
    if os.path.exists(outdir) and os.listdir(outdir):
        echo('{0}', 'Output directory is not empty', color=Fore.RED)
        return
    os.makedirs(sample_dir)

    echo('Using library at {0}', library, color=Fore.CYAN)

    files = []
    for fmt in formats:
        files += glob(os.path.join(library, '*.{0}'.format(fmt)))

    echo('Working with {0} songs', len(files))

    random.shuffle(files)

    # Select a song to base the mix around
    if focal is None:
        focal = files.pop()
    else:
        files = [f for f in files if f != focal]
    focal_bpm, focal_key = analysis.analyze(focal)

    echo('\nFocal song: {0}', focal, color=Fore.YELLOW)
    echo('\tBPM: {0}', focal_bpm)
    echo('\tKey: {0} ({1})', focal_key.key, focal_key.scale)

    # Search for songs that require relatively small modifications
    # to match the focal song
    bpm_range_l = 0.85 * focal_bpm
    bpm_range_u = 1.15 * focal_bpm
    key_range = 6

    # Select appropriate songs to mix
    n = n_songs if n_songs is not None else random.randint(n_tracks+2, n_tracks+6)
    selections = []
    echo('\nSelecting {0} other songs', n)

    while len(selections) < n and files:
        song = files.pop()
        bpm, key = analysis.analyze(song)
        echo('Analyzing {0}', song, color=Fore.CYAN)
        if bpm_range_l <= bpm <= bpm_range_u and (focal_key.mixable(key) or abs(focal_key.distance(key)) <= key_range):
            echo('\t{0}', 'OK')
            selections.append((song, bpm, key))
        else:
            echo('\tSkipping')

    # Mutate songs as needed and generate samples
    echo('\n{0}', 'Processing songs', color=Fore.YELLOW)
    slices = {}
    for song, bpm, key in selections + [(focal, focal_bpm, focal_key)]:
        filename = os.path.basename(song)
        name, ext = os.path.splitext(filename)
        echo('Processing {0}', filename, color=Fore.CYAN)

        # Copy over files
        outfile = os.path.join(outdir, filename)
        shutil.copy(song, outfile)
        tmpfile = os.path.join(outdir, '{0}.tmp{1}'.format(name, ext))

        # Process as necessary
        if not focal_key.mixable(key):
            echo('\tChanging key')
            mutate.key_shift(outfile, key, focal_key, tmpfile)
            shutil.move(tmpfile, outfile)

        if focal_bpm != bpm:
            echo('\tChanging bpm')
            mutate.tempo_stretch(outfile, bpm, focal_bpm, tmpfile)
            shutil.move(tmpfile, outfile)

        # Trim silence
        echo('\tTrimming silence')
        mutate.trim_silence(outfile, tmpfile)
        shutil.move(tmpfile, outfile)

        # Slice according to beats
        echo('\tSlicing')
        beats = analysis.estimate_beats(outfile)

        # If debug is set, add click track to check beat alignment
        if debug:
            mutate.add_click(outfile, beats, tmpfile)
            shutil.move(tmpfile, outfile)

        song_sample_dir = os.path.join(sample_dir, name)
        os.makedirs(song_sample_dir)

        # Assemble samples of the smallest sample size
        # They will be combined later into larger samples
        prefix = '{0}_{1}_'.format(name, min_sample_size)
        slices[name] = [Slice(f) for f in mutate.beat_slice(outfile,
                                                           beats,
                                                           min_sample_size,
                                                           song_sample_dir,
                                                           prefix=prefix,
                                                           format=ext)]

    # Remove samples which have irregular duration
    slices = heuristics.filter_slices(slices)

    # Build songs + samples out of the slices
    # Some songs may return no slices, in which case, ignore that song.
    songs = [Song(nm, slics, sample_sizes) for nm, slics in slices.items() if any(s is not None for s in slics)]

    # Select samples and assemble tracks
    echo('\n{0}', 'Assembling tracks', color=Fore.YELLOW)
    tracks, tracklist = producer.produce_tracks(songs,
                                                outdir,
                                                length=length,
                                                coherent=not incoherent,
                                                n_tracks=n_tracks)

    # Overlay the tracks
    echo('{0}', 'Assembling mix', color=Fore.YELLOW)

    mix_file = os.path.join(outdir, '_mix.mp3')
    producer.produce_mix(tracks, mix_file, format='mp3')

    # Write the tracklist
    tracklisting = '\n\n---\n\n'.join(['\n'.join(['{0}\t{1}'.format(t, s) for t, s in tl]) for tl in tracklist])
    trl_file = os.path.join(outdir, '_tracklist.txt')
    with open(trl_file, 'w') as f:
        f.write(tracklisting)

    echo('\n{0}', 'The new pablo track just dropped ~ (done)')
