import os
import sys

def fetch_photo_names(tar_directory, eof='png'):

    photo_list = [name for name in os.listdir(tar_directory)
                  if name.endswith(eof)]
    return photo_list


def photo_rename(photonames, directory, tar_directory):

    #old_photonames = os.path.join(directory, photonames + '.png')
    #new_photonames = os.path.join(directory, "FF4_2016-08-31-07-59_photo_" + photonames + '.png')

    os.rename(tar_directory + photonames, directory + "FF4_2016-08-31-07-59_photo_" + photonames)


if __name__ == '__main__':

    tar_directory = '/Users/lizhijun/Downloads/FF4_2016-08-31-07-59_photo/'
    directory = '/Users/lizhijun/Downloads/FF4_2016-08-31-07-59-photo/'
    photo_list = fetch_photo_names(tar_directory)
    for photonames in photo_list:
        print (photonames)

        photo_rename(photonames, directory, tar_directory)