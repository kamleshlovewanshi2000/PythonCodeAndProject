# # # s = "welcome to Truba"
# # # #Slicing
# # #
# # # # print(s[-1::-1])
# # # # print(s[::2])
# # # # print(s[7:2:-1])
# # #
# # # # Functions Used
# # #
# # # l = s.lower()
# # # u = s.upper()
# # # t = s.title()
# # # c = s.capitalize()
# # # print(l)
# # # print(u)
# # # print(t)
# # # print(c)
# #
# # w = "Welcome"
# # d = "11354"
# # ad = "321GoCheck"
# # print(w.isalpha())
# # print(d.isdigit())
# # print(ad.isalnum())
# #
# # # Use of chr() Function
# # d = 90
# # print(chr(d))
# # for i in range(65,91):
# #     print(chr(i),end=" ")
# # print("\n")
# # for i in range(91,97):
# #     print(chr(i),end=" ")
# # print("\n")
# # for i in range(97,123):
# #     print(chr(i),end=" ")
# # print("\n")
# # for i in range(123,150):
# #     print(chr(i),end=" ")
#
# # Use of ord() Function
#
# n = "M"
# print(ord(n))

# String Formatting
fname = input("Enter your First name :")
lname = input("Enter your last name :")
loc = input("Enter your Location :")
text = '''Hello sir
        I am {fname:^10} {lname:>20}
        I am from {loc:<10}
        '''.format(fname=fname,lname=lname,loc=loc)

print(text)
