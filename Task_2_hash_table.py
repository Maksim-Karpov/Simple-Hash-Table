from math import sqrt
import hashlib
# Реализация хеш-таблицы в Python
table_size = 10

#Создание хеш-таблицы
hashTable = [[],] * table_size

KNUTH_CONST = (sqrt(5)-1)/2

#Упрощённая реализация хэш-таблиц
class HashTable:
    def __init__(self, table_size, type):
        self.size = table_size
        self.type = type
        self.table = {}
        #Создание словаря
        for i in range(self.size):    
            self.table[str(i)] = "_" #[{i:_} for i in range(self.size)]
        print("Hash Table Initialized !")

    def PrintTable(self):
        print(self.table)

    # methods = "division", "multiplication", "universal hash"
    def AddElement(self, element):
        key = self.BreakDownWord(element)
        if self.type == "division":
            index = self.DivisionMethod(key)
        elif self.type == "multiplication":
            index = self.MultiplicationMethod(key)
        elif self.type == "universal hash":
            index = self.HashCryptography(element)
        self.table.update({str(index): element})
        

    #Преобзразование записи в сумму кодов ascii
    def BreakDownWord(self, input):
        ascii_sum = 0
        #print(f'word: {input}. ascii:')
        for char in input:
            ascii_symb = int(ord(char))
            #print(f'{char} -> {ascii_symb}')
            ascii_sum += ascii_symb
        #print(ascii_sum)
        return ascii_sum #Это и есть ключ, который дальше будет делиться

    def MultiplicationMethod(self, key):
        hash_index = round(self.size * ((key * KNUTH_CONST) % 1)) # расчёт индекса через метод умножения
        print("Mult method. Index = " + str(hash_index))
        return hash_index
    
    def DivisionMethod(self, key):
        #print(f'{key} mod {self.size} = ')
        hash_index = key % self.size
        print("Division method. Index = " + str(hash_index))
        return hash_index

    def HashCryptography(self, element):
        hash_string = hashlib.md5(element.encode('utf8')).hexdigest()
        #print(f'{element} -> {hash_string}')
        hash_int = int(hash_string, 16)
        #print(hash_int)
        hash_index = hash_int % self.size
        print("Hash Cryptography method. Index = " + str(hash_index))
        return hash_index

    def GetElement(self, element):
        key = self.BreakDownWord(element)
        if self.type == "division":
            index = self.DivisionMethod(key)
        elif self.type == "multiplication":
            index = self.MultiplicationMethod(key)
        elif self.type == "universal hash":
            index = self.HashCryptography(element)
        print(self.table[str(index)])
        
print("---DIVISION METHOD---")
hash_table_div = HashTable(table_size, type = "division")
#hash_table_div.PrintTable()
#Добавление записи
hash_table_div.AddElement(element="Rae")
hash_table_div.AddElement(element="Bartholomeu")
hash_table_div.AddElement(element="Ivan")
hash_table_div.AddElement(element="Bufford")
hash_table_div.AddElement(element="Jonathan")

hash_table_div.PrintTable()
hash_table_div.GetElement("Jonathan")

print("---MULTIPLICATION METHOD---")
hash_table_mult = HashTable(table_size, type = "multiplication")
hash_table_mult.AddElement(element="Beatrice")
hash_table_mult.AddElement(element="Sergey")
hash_table_mult.AddElement(element="Alexander")
hash_table_mult.AddElement(element="Paul")
hash_table_mult.AddElement(element="Zoe")
hash_table_mult.PrintTable()
hash_table_mult.GetElement("Beatrice")

print("---CRYPTOGRAOHIC HASH FUNCTION METHOD---")
hash_table_hash = HashTable(table_size, type="universal hash")
hash_table_hash.AddElement("John")
hash_table_hash.AddElement("Zero")
hash_table_hash.AddElement("Katherine")
hash_table_hash.AddElement("Shaun")
hash_table_hash.PrintTable()

hash_table_hash.GetElement("Dimitry")

