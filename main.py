import os
import csv


def main():

    dirName = 'C:/Users/crm0135/PycharmProjects/pythonProject/PRG_ANALISI_OBS'

    def list_files(startpath):
        row_list = []
        for root, dirs, files in os.walk(startpath):
            count = 0
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            directory_name = ('{}{}'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                count += 1
                #print('{}{}'.format(subindent, f))
            row_list.append([directory_name, count])

        return row_list


    csv_row = list_files(dirName)
    csv_row.pop(0)

    out = open('out.csv', 'w')
    out.write('Dirname; Count of files\n')
    for row in csv_row:
        for column in row:
            out.write('%s;' % column)

        out.write('\n')

    out.close()


if __name__ == '__main__':
    main()