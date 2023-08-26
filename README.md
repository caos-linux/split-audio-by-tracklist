# split-audio-by-tracklist

The script splits a big audio file into a set of tracks with varying lengths, according to a tracklist file.

This is a modified version of the script "split.py" found here: https://unix.stackexchange.com/questions/280767/how-do-i-split-an-audio-file-into-multiple .

usage: ./split.py <original_track> <track_list>

where

* original_track is Mozart.m4a

* track_list is like this:

tracklist.txt
```
# Mozart Akademie Amsterdam
# Jaap ter Linden (conductor)
00:00:00 Symphony No.1 in E-Flat, K. 16: I. Molto allegro
00:05:58 Symphony No.1 in E-Flat, K. 16: II. Andante
00:11:01 Symphony No.1 in E-Flat, K. 16: III. Presto
00:12:42 Symphony in F, K. 19 A: I. Allegro assai
00:17:46 Symphony in F, K. 19 A: II. Andante
00:22:29 Symphony in F, K. 19 A: III. Presto
00:24:00 Symphony No. 6 in F, K. 43: I. Allegro
00:29:31 Symphony No. 6 in F, K.43: II. Andante
00:34:45 Symphony No. 6 in F, K. 43: III. Menuetto & trio
00:36:43 Symphony No. 6 in F, K. 43: IV. Allegro
00:40:33 Symphony No. 45 in D, K. 45: I. Molto allegro
00:43:11 Symphony No. 45 in D, K. 45: II. Andante
00:45:10 Symphony No. 45 in D, K. 45: III. Menuetto & trio
00:48:54 Symphony No. 45 in D, K. 45: IV. Molto allegro
```

The script will produce these files:

```
01 - symphony-no1-in-e-flat-k-16-i-molto-allegro.m4a
02 - symphony-no1-in-e-flat-k-16-ii-andante.m4a
03 - symphony-no1-in-e-flat-k-16-iii-presto.m4a
04 - symphony-in-f-k-19-a-i-allegro-assai.m4a
05 - symphony-in-f-k-19-a-ii-andante.m4a
06 - symphony-in-f-k-19-a-iii-presto.m4a
07 - symphony-no-6-in-f-k-43-i-allegro.m4a
08 - symphony-no-6-in-f-k43-ii-andante.m4a
09 - symphony-no-6-in-f-k-43-iii-menuetto-trio.m4a
10 - symphony-no-6-in-f-k-43-iv-allegro.m4a
11 - symphony-no-45-in-d-k-45-i-molto-allegro.m4a
12 - symphony-no-45-in-d-k-45-ii-andante.m4a
13 - symphony-no-45-in-d-k-45-iii-menuetto-trio.m4a
14 - symphony-no-45-in-d-k-45-iv-molto-allegro.m4a
```
