# # def destCity(paths=[[]]):
# #     result = ''
# #     print(paths)
# #     # print(destiny)
# #     for i in paths:
# #         print(i)
# #         for j in i:
# #             print(j)
# #             result = j
# #     return print(result)
# # paths= [['a','s'],['e','u']]

# class Solution:
#     # def sortArrayByParity(self, A=[3,1,2,4]):
#     #     #declarar variables una para pares y otra para impares.
#     #     pares = []
#     #     impares = []

#     #     #for recorrer la lista y separarlos
#     #     for i in A:
#     #         if i % 2 == 0:
#     #             pares.append(i)
#     #         else:
#     #             impares.append(i)

#     #     #juntar la lista y retornar el output que nos piden.
#     #     return print(pares + impares)
#     def sortArrayByParity(self, A=[3, 1, 2, 4]):
#     # juntar la lista y retornar el output que nos piden.
#         return print(sorted(A, key = lambda x : x % 2))
# Subdomain Visit Count

###############
## Generate Parentheses
## Given n pairs of parentheses, write a function to generate all
#  combinations of well-formed parentheses.
##############

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

###############

def genParentheses(num):
    ###### FIRST TRY
    # result = []
    # for i in range(num):
    #     result.append("()")
    # return print(result)
    ###### SECOND TRY
    # """ Assumes 1 <= n <= 8 """
    # possibilities = {}
    # result = []
    # for i in range(num):
    #     result.append("()")
    #     print('i:', i)
    #     print('len of result:', len(result))
    #     possibilities[i+1] = result
    #     print (possibilities.items())
    #     for j in result:
    #         if '(' in result[j]:
    ###### THIRD TRY
    """         SI me pasa 1 armo ()
                si me pasa 2 armo () y (()), ()()
                osea, si se encuentra con ( 
                    agrega otro ( justo antes de (
                        agrega otro ( justo despues de ) 
    """
    result = []
    temp = []
    if num == 1:
        return ['()']
    else:
        while num > 0:
            result.append('()')
            num -= 1
        for i in result:
            for '(' in result[i]:
                temp[i] = str(result[i])
    print(temp)


    
    return print(result)

if __name__ == '__main__':
    # destCity([['a','s'],['e','u']])
    # Solution.sortArrayByParity([3, 1, 2, 4])
    genParentheses(3)