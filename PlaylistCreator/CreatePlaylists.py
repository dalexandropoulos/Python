import os

def create_playlists_recursive(folder_path, extensions, copyright):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if any(file.lower().endswith(tuple(extensions)) for file in os.listdir(dir_path)):
                create_playlist(dir_path, extensions, copyright)

def create_playlist(folder_path, extensions, copyright_text):
    playlist_name = os.path.join(folder_path, os.path.basename(folder_path) + '.pls')
    playlist_file = open(playlist_name, 'w', encoding='utf-8')
    playlist_file.write('[playlist]\n')
    playlist_file.write('NumberOfEntries=0\n')  # initialize the number of entries to 0
    if copyright_text:
        playlist_file.write('Comment=%s\n' % copyright_text)
    index = 1
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(tuple(extensions)):
                media_file_path = os.path.join(root, file)
                media_file_name = os.path.basename(media_file_path)
                playlist_file.write('File%d=%s\n' % (index, media_file_name))
                playlist_file.write('Title%d=%s\n' % (index, os.path.splitext(media_file_name)[0]))
                index += 1
    playlist_file.write('NumberOfEntries=%d\n' % (index - 1))
    playlist_file.write('Version=2\n')
    playlist_file.close()

# Example usage: create playlists for the current folder and its subfolders for mp3, mp4, avi, mkv and flac files
extensions = ('.mp3', '.mp4', '.avi', '.mkv', '.flac')
copyright = 'Copyright (c) 2023 Alexandropoulos Dimitrios'
current_folder_path = os.getcwd()
create_playlists_recursive(current_folder_path, extensions, copyright)


# Testing Done !