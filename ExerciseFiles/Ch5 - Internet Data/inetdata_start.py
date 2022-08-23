# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request # for http requests
def main():
   weburl = urllib.request.urlopen("http://www.google.com") # 200 running fine. 404 error not found etc
   print("Result code:", weburl.getcode())
   data = weburl.read()
   print(data)
   #read data and print it out to terminal. Data of Googles home page

   

if __name__ == "__main__":
    main()
