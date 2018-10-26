# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:54:42 2018

@author: Jing
"""

import Car
import DoubleLinkedList
# Test 
menulist = ['Enter: ',
		'1  for Search', 
		'2  for Deletion', 
		'3  for Append to head', 
		'4  for Append to tail', 
		'5  for Remove from head', 
		'6  for Remove from tail',
       '7  for Print']
def menu():
	for i in range(len(menulist)):
		print(menulist[i])
	return int(input())

def Main():
    DLL = DoubleLinkedList.DoubleLinkedList()
    try:
        fo = open("Cars.txt", "r")
    except IOError:
        print("No such file!")
    else:
        for line in fo.readlines():
            info = line.split()
            Make = info[0]
            Model = info[1]
            Year = int(info[2])
            Mileage = float(info[3])
            Price = float(info[4])
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            DLL.AppendToHead(newCar)
        fo.close()
    print("Cars information in the system are as follows:")
    DLL.PrintCars()    
    s = menu()
    while s in range(1,8):
        if s == 1:
            key = float(input("Enter car's price you want to search:"))
            foundNode = DLL.Search(key)
            if (foundNode != 0):
                print("The car information you want to search are Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" %(foundNode.data.Make, foundNode.data.Model, foundNode.data.Year, foundNode.data.Mileage, foundNode.data.Price))
            else:
                print("There is no such car with price of ", key)
        if s == 2:
            key = float(input("Enter the car price you want to delete: "))
            t = DLL.Delete(key)
            if t == 1:
                print("The car with the price has been deleted!")
            DLL.PrintCars()
        if s == 3:
            print("Enter the information of the car you want to append to the head:")
            Make = input("Make: ")
            Model = input("Model: ")
            Year = int(input("Year: "))
            Mileage = float(input("Mileage: "))
            Price = float(input("Price: "))
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            DLL.AppendToHead(newCar)
            print("Cars information in the system are as follows: ")
            DLL.PrintCars()
        if s == 4:
            print("Enter the information of the car you want to append to the tail:")
            Make = input("Make: ")
            Model = input("Model: ")
            Year = int(input("Year: "))
            Mileage = float(input("Mileage: "))
            Price = float(input("Price: "))
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            DLL.AppendToTail(newCar)
            print("Cars information in the system are as follows: ")
            DLL.PrintCars()
        if s == 5:
            oldCar = DLL.RemoveFromHead()
            if oldCar != 0:
                print("Removed car information from Head are Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" %(oldCar.data.Make, oldCar.data.Model, oldCar.data.Year, oldCar.data.Mileage, oldCar.data.Price))
        if s == 6:
            oldCar = DLL.RemoveFromTail()
            if oldCar != 0:
                print("Removed car information from Tail are Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" %(oldCar.data.Make, oldCar.data.Model, oldCar.data.Year, oldCar.data.Mileage, oldCar.data.Price))
        if s == 7:
            DLL.PrintCars()
        s = menu()
Main()