import os
import sys


def file_to_dic(filename):
    """

    :arg
        filename(.txt file) - parameter

    :return:
        a dictionary, key=id and value=[password, balance]

    """
    atm = {}
    with open(filename, 'r') as file:
        for line in file:
            details = line.strip().split(' ')
            atm[details[0]] = details[1:]

    return atm


def atm_machine(id, atm_dic):
    """

    Args:
        id (str)- first parameter
        atm_dic (dic)- second parameter

    :return:
        A dictionary with the updated values
        after performing the desired action

    """
    if atm_dic.get(id):
        action = input("enter number of action:\n"
                       "1- for check the balance\n"
                       "2- for cash withdrawal\n"
                       "3- for cash deposit\n"
                       "4- for change password\n")

        if action == '1':
            print(f"your balance is: {atm_dic[id][1]}")

        elif action == '2':
            money = input("enter the amount you want to withdraw\n")
            atm_dic[id][1] = str(int(atm_dic[id][1]) - int(money))

        elif action == '3':
            money = input("enter the amount you want to deposit\n")
            atm_dic[id][1] = str(int(atm_dic[id][1]) + int(money))

        elif action == '4':
            password = input('enter new password\n')
            atm_dic[id][0] = password

        else:
            print('action not detected')

    else:
        print('there is an error i the ID you etered')


def main():
    """

    :arg
        id(int) - 9 digits ID (example: 322781145)

    :return:
        will do the desired ATM operation accordig to an
        ID that has been accepted until receive -1 as an ID.
        all the chages will be saved to the ATM.

    """
    if os.path.isfile(sys.argv[1]):
        atm_dic = file_to_dic(sys.argv[1])
        id = input('please enter your ID\n')

        while id != '-1':
            atm_machine(id, atm_dic)
            id = input('please enter your ID\n')

        with open(sys.argv[1],'w') as newfile:
            for id in atm_dic:
                newfile.writelines(f"{id} {atm_dic[id][0]} {atm_dic[id][1]}\n")

    else:
        print('file not found')


if __name__ == '__main__':
    main()