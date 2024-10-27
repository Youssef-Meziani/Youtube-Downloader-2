from pytube import YouTube
from time import sleep
from colorama import Fore, Style
import shutil
import colorama
import ffmpeg
import socket
import itertools
import threading
import subprocess
import os
import ctypes

colorama.init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Youtube Video downloader - by Youssef Meziani")


def animate():
    global done
    global ext
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        if ext == "mp4" or ext == "webm":
            print("\r\u001b[35mMerging Video with Audio\u001b[0m..." + c, end="")
        else:
            print("\r\u001b[35mConverting to mp3\u001b[0m..." + c, end="")
        sleep(0.1)


def check_internet():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except OSError:
        return False


def quality_mp4():
    qua_mp4 = []
    if yt.streams.get_by_itag(571) or yt.streams.get_by_itag(402):
        qua_mp4.append("8k")
    if yt.streams.get_by_itag(401) or yt.streams.get_by_itag(305) or yt.streams.get_by_itag(266):
        qua_mp4.append("4k")
    if yt.streams.get_by_itag(400) or yt.streams.get_by_itag(304) or yt.streams.get_by_itag(264):
        qua_mp4.append("qhd")
    if yt.streams.get_by_itag(399) or yt.streams.get_by_itag(299) or yt.streams.get_by_itag(137):
        qua_mp4.append("fhd")
    if yt.streams.get_by_itag(398) or yt.streams.get_by_itag(298) or yt.streams.get_by_itag(136):
        qua_mp4.append("720p")
    if yt.streams.get_by_itag(397) or yt.streams.get_by_itag(135):
        qua_mp4.append("480p")
    if yt.streams.get_by_itag(396) or yt.streams.get_by_itag(134):
        qua_mp4.append("360p")
    if yt.streams.get_by_itag(395) or yt.streams.get_by_itag(133):
        qua_mp4.append("240p")
    if yt.streams.get_by_itag(394) or yt.streams.get_by_itag(160):
        qua_mp4.append("144p")
    print("\nSelect quality to download [",end="")
    print("] [".join(qua_mp4),end="")
    choi = input("] : ").strip().lower()
    while True:
        if choi in qua_mp4:
            break
        else:
            choi = input(f"{red}Invalid Quality,{r} Try Again : ").strip().lower()
    return choi


def quality_webm():
    qua_webm = []
    if yt.streams.get_by_itag(272):
        qua_webm.append("8k")
    if yt.streams.get_by_itag(337) or yt.streams.get_by_itag(315) or yt.streams.get_by_itag(313):
        qua_webm.append("4k")
    if yt.streams.get_by_itag(336) or yt.streams.get_by_itag(308) or yt.streams.get_by_itag(271):
        qua_webm.append("qhd")
    if yt.streams.get_by_itag(335) or yt.streams.get_by_itag(303) or yt.streams.get_by_itag(248):
        qua_webm.append("fhd")
    if yt.streams.get_by_itag(334) or yt.streams.get_by_itag(302) or yt.streams.get_by_itag(247):
        qua_webm.append("720p")
    if yt.streams.get_by_itag(333) or yt.streams.get_by_itag(244):
        qua_webm.append("480p")
    if yt.streams.get_by_itag(332) or yt.streams.get_by_itag(243):
        qua_webm.append("360p")
    if yt.streams.get_by_itag(331) or yt.streams.get_by_itag(242):
        qua_webm.append("240p")
    if yt.streams.get_by_itag(330) or yt.streams.get_by_itag(278):
        qua_webm.append("144p")
    print("\nSelect quality to download [", end="")
    print("] [".join(qua_webm), end="")
    choi = input("] : ").strip().lower()
    while True:
        if choi in qua_webm:
            break
        else:
            choi = input(f"{red}Invalid Quality,{r} Try Again : ").strip().lower()
    return choi


while True:
    os.system("cls")
    r = Fore.RESET
    red = Fore.RED
    gr = Fore.GREEN
    bl = Fore.BLUE
    ma = Fore.MAGENTA
    yl = Fore.YELLOW
    done = False

    while True:
        if not check_internet():
            input(f"{red}Please check your internet connection,{r} Then press ENTER to try again :")
        else:
            break

    url = input(f"{Style.BRIGHT}Enter The Youtube URL : ")
    while True:
        try:
            print(f"{ma}Getting URL Info{r}...", end="")
            if True:
                yt = YouTube(url)
                break
        except:
            print(f"{red}Failed{r}")
            url = input(f"{red}Invalid Youtube URL,{r} Try again : ")
    print(f"{gr}Done")

    print(f"\n{bl}Video Title : {r}", yt.title)
    print(f"{bl}Video length : {r}", round(yt.length/60, 2), "min")
    views = yt.views
    if views >= 1000000:
        print(f"{bl}Video Views : {r}"+str(round(views/1000000, 2))+"M")
    elif views >= 1000:
        print(f"{bl}Video Views : {r}"+str(int(views/1000))+"K")
    elif views < 1000:
        print(f"{bl}Video Views : {r}", views)
    publish_date = str(yt.publish_date)
    print(f"{bl}Video Publish Date : {r}", publish_date[:10])
    print(f"{bl}Video Author : {r}", yt.author)

    path = os.getcwd() + r"\Downloads"
    x = yt.title
    x = x.replace("<", "").replace(">", "").replace(":", "").replace("\\", "").replace("/", "").replace("*", "")\
        .replace("?", "").replace("|", "").replace("\"", "").replace(".", "")
    folder = x
    file = x

    ext = input("\nSelect File extension ([mp4] or [webm] for Video or [mp3] for Audio) : ").strip().lower()
    while True:
        if ext == "mp4" or ext == "webm" or ext == "mp3":
            break
        else:
            ext = input(f"{red}Invalid File Extension,{r} Try Again : ").strip().lower()

    if ext == "mp4" or ext == "webm":
        if ext == "mp4":
            choice = quality_mp4()


            def _8k():
                try:
                    yt.streams.get_by_itag(571).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(402).download(fr'{path}\{file}')


            def _4k():
                try:
                    yt.streams.get_by_itag(401).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(305).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(266).download(fr'{path}\{file}')


            def _qhd():
                try:
                    yt.streams.get_by_itag(400).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(304).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(264).download(fr'{path}\{file}')


            def _fhd():
                try:
                    yt.streams.get_by_itag(399).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(299).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(137).download(fr'{path}\{file}')


            def _720p():
                try:
                    yt.streams.get_by_itag(398).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(298).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(136).download(fr'{path}\{file}')


            def _480p():
                try:
                    yt.streams.get_by_itag(397).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(135).download(fr'{path}\{file}')


            def _360p():
                try:
                    yt.streams.get_by_itag(396).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(134).download(fr'{path}\{file}')


            def _240p():
                try:
                    yt.streams.get_by_itag(395).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(133).download(fr'{path}\{file}')


            def _144p():
                try:
                    yt.streams.get_by_itag(394).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(160).download(fr'{path}\{file}')


            def _8k_size():
                try:
                    size = round(yt.streams.get_by_itag(571).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(402).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _4k_size():
                try:
                    size = round(yt.streams.get_by_itag(401).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(305).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(266).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _qhd_size():
                try:
                    size = round(yt.streams.get_by_itag(400).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(304).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(264).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _fhd_size():
                try:
                    size = round(yt.streams.get_by_itag(399).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(299).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(137).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _720p_size():
                try:
                    size = round(yt.streams.get_by_itag(398).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(298).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(136).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _480p_size():
                try:
                    size = round(yt.streams.get_by_itag(397).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(135).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _360p_size():
                try:
                    size = round(yt.streams.get_by_itag(396).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(134).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _240p_size():
                try:
                    size = round(yt.streams.get_by_itag(395).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(133).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _144p_size():
                try:
                    size = round(yt.streams.get_by_itag(394).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(160).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
        else:
            choice = quality_webm()


            def _8k():
                yt.streams.get_by_itag(272).download(fr'{path}\{file}')


            def _4k():
                try:
                    yt.streams.get_by_itag(337).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(315).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(313).download(fr'{path}\{file}')


            def _qhd():
                try:
                    yt.streams.get_by_itag(336).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(308).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(271).download(fr'{path}\{file}')


            def _fhd():
                try:
                    yt.streams.get_by_itag(335).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(303).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(248).download(fr'{path}\{file}')


            def _720p():
                try:
                    yt.streams.get_by_itag(334).download(fr'{path}\{file}')
                except:
                    try:
                        yt.streams.get_by_itag(302).download(fr'{path}\{file}')
                    except:
                        yt.streams.get_by_itag(247).download(fr'{path}\{file}')


            def _480p():
                try:
                    yt.streams.get_by_itag(333).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(244).download(fr'{path}\{file}')


            def _360p():
                try:
                    yt.streams.get_by_itag(332).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(243).download(fr'{path}\{file}')


            def _240p():
                try:
                    yt.streams.get_by_itag(331).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(242).download(fr'{path}\{file}')


            def _144p():
                try:
                    yt.streams.get_by_itag(330).download(fr'{path}\{file}')
                except:
                    yt.streams.get_by_itag(278).download(fr'{path}\{file}')


            def _8k_size():
                size = round(yt.streams.get_by_itag(272).filesize * 9.5367431640625e-7, 2)
                return print(f"{size}MB....", end="")


            def _4k_size():
                try:
                    size = round(yt.streams.get_by_itag(337).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(315).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(313).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _qhd_size():
                try:
                    size = round(yt.streams.get_by_itag(336).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(308).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(271).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _fhd_size():
                try:
                    size = round(yt.streams.get_by_itag(335).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(303).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(248).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _720p_size():
                try:
                    size = round(yt.streams.get_by_itag(334).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    try:
                        size = round(yt.streams.get_by_itag(302).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")
                    except:
                        size = round(yt.streams.get_by_itag(247).filesize * 9.5367431640625e-7, 2)
                        return print(f"{size}MB....", end="")


            def _480p_size():
                try:
                    size = round(yt.streams.get_by_itag(333).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(244).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _360p_size():
                try:
                    size = round(yt.streams.get_by_itag(332).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(243).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _240p_size():
                try:
                    size = round(yt.streams.get_by_itag(331).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(242).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")


            def _144p_size():
                try:
                    size = round(yt.streams.get_by_itag(330).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")
                except:
                    size = round(yt.streams.get_by_itag(278).filesize * 9.5367431640625e-7, 2)
                    return print(f"{size}MB....", end="")

        i = 1
        while os.path.exists(fr'{path}\{folder}'):
            op = input(f"{red}Video folder already exist,{r} Type  {yl}1:{r} To replace it   {yl}2:{r} To rename it : "
                       ).strip().lower()
            while True:
                try:
                    if int(op) == 1 or int(op) == 2:
                        break
                    else:
                        op = input(f"{red}Out of range,{r} Type  {yl}1:{r} To replace it  {yl}2:{r} To rename it : "). \
                            strip().lower()
                except ValueError:
                    op = input(
                        f"{red}Only numbers,{r} Type  {yl}1:{r} To replace it  {yl}2:{r} To rename it : ").strip(). \
                        lower()
            if op == '1':
                shutil.rmtree(fr'{path}\{folder}')
                break
            elif op == '2':
                while os.path.exists(fr'{path}\{folder}'):
                    folder = file + f"({i})"
                    i += 1

        audio = yt.streams.get_by_itag(251)
        print(f"\n{ma}Downloading Audio{r}..." + str(round(audio.filesize * 9.5367431640625e-7, 2)) + "MB...", end="")
        audio.download(fr'{path}\{folder}')
        subprocess.check_call(["attrib", "+H", fr'{path}\{folder}\{file}.webm'])
        os.rename(fr'{path}\{folder}\{file}.webm', fr'{path}\{folder}\Downloaded_Audio.webm')
        print(f"{gr}Done")

        if choice == '8k':
            print(f"{ma}Downloading 8k{r}...", end="")
            _8k_size()
            _8k()
            print(f"{gr}Done")
        elif choice == '4k':
            print(f"{ma}Downloading 4k{r}...", end="")
            _4k_size()
            _4k()
            print(f"{gr}Done")
        elif choice == 'qhd':
            print(f"{ma}Downloading qhd{r}...", end="")
            _qhd_size()
            _qhd()
            print(f"{gr}Done")
        elif choice == 'fhd':
            print(f"{ma}Downloading fhd{r}...", end="")
            _fhd_size()
            _fhd()
            print(f"{gr}Done")
        elif choice == '720p':
            print(f"{ma}Downloading 720p{r}...", end="")
            _720p_size()
            _720p()
            print(f"{gr}Done")
        elif choice == '480p':
            print(f"{ma}Downloading 480p{r}...", end="")
            _480p_size()
            _480p()
            print(f"{gr}Done")
        elif choice == '360p':
            print(f"{ma}Downloading 360p{r}...", end="")
            _360p_size()
            _360p()
            print(f"{gr}Done")
        elif choice == '240p':
            print(f"{ma}Downloading 240p{r}...", end="")
            _240p_size()
            _240p()
            print(f"{gr}Done")
        elif choice == '144p':
            print(f"{ma}Downloading 144p{r}...", end="")
            _144p_size()
            _144p()
            print(f"{gr}Done")

        subprocess.check_call(["attrib", "+H", fr'{path}\{folder}\{file}.{ext}'])
        os.rename(fr'{path}\{folder}\{file}.{ext}', fr'{path}\{folder}\Downloaded_Video.{ext}')
        threading.Thread(target=animate).start()

        vid = ffmpeg.input(fr'{path}\{folder}\Downloaded_Video.{ext}')
        aud = ffmpeg.input(fr'{path}\{folder}\Downloaded_Audio.webm')
        ffmpeg.output(vid, aud, fr'{path}\{folder}\{file}.{ext}', vcodec='copy', loglevel="quiet").run()

        os.remove(fr'{path}\{folder}\Downloaded_Audio.webm')
        os.remove(fr'{path}\{folder}\Downloaded_Video.{ext}')

        done = True
        print(f"\r{ma}Merging Video with Audio{r}...{gr}Done\n")
    else:
        i = 1
        while os.path.exists(fr'{path}\{file}.mp3'):
            op = input(f"{red}Audio file already exist,{r} Type  {yl}1:{r} To replace it   {yl}2:{r} To rename it : ").\
                strip().lower()
            while True:
                try:
                    if int(op) == 1 or int(op) == 2:
                        break
                    else:
                        op = input(f"{red}Out of range,{r} Type  {yl}1:{r} To replace it  {yl}2:{r} To rename it : "). \
                            strip().lower()
                except ValueError:
                    op = input(
                        f"{red}Only numbers,{r} Type  {yl}1:{r} To replace it  {yl}2:{r} To rename it : ").strip(). \
                        lower()
            if op == '1':
                os.remove(fr'{path}\{file}.mp3')
                break
            elif op == '2':
                while os.path.exists(fr'{path}\{file}.mp3'):
                    file = folder + f"({i})"
                    i += 1

        audio = yt.streams.get_by_itag(251)
        print(f"\n{ma}Downloading Audio{r}..." + str(round(audio.filesize * 9.5367431640625e-7, 2)) + "MB...", end="")
        audio.download(fr'{path}')
        subprocess.check_call(["attrib", "+H", fr'{path}\{folder}.webm'])
        os.rename(fr'{path}\{folder}.webm', fr'{path}\Downloaded_Audio.webm')
        print(f"{gr}Done")

        threading.Thread(target=animate).start()

        aud = ffmpeg.input(fr'{path}\Downloaded_Audio.webm')
        ffmpeg.output(aud, fr'{path}\{file}.mp3', loglevel="quiet").run()

        os.remove(fr'{path}\Downloaded_Audio.webm')

        done = True
        print(f"\r{ma}Converting to mp3{r}...{gr}Done\n")

    print('=' * 19)
    print(f"{gr}Download Completed")
    print('=' * 19)
    print(f"\nYou can find the video in : {path}")

    action = input(f"\n{Style.BRIGHT}You Want To Download Another Video (y/n) ? ").strip().lower()
    while True:
        if action == 'n' or action == 'no':
            print("\nThanks for downloading :)")
            s = 3
            while s >= 0:
                print("\rExit in " + str(s), end="")
                sleep(1)
                s -= 1
            exit()
        elif action == 'y' or action == 'yes':
            break
        action = input(f"{red}Invalid Input,{r} {Style.BRIGHT}You Want To Download Another Video (y/n) ?").strip().\
            lower()
