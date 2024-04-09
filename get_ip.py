import requests
import os

class Ipv4AddressManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def GetIpv4Address(self) -> str:
        Ipv4_r = requests.get("http://ifconfig.me")

        if Ipv4_r.status_code == 200:
            print("[+] GET request succesfully sent.")
            
            return Ipv4_r.text
        else:
            print("[!] Connection may have not worked, try again.")

            return "Error"
    
    def Store_Ipv4(self) -> str:
        if self.mode == ".":
            file_name = "ipv4.txt"

            ipv4_result = self.GetIpv4Address()

            if ipv4_result == "Error":
                
                return ""

            try:
                file = open(file_name, "w")

            except PermissionError as PE:
                print("Error: " + str(PE))

                return ""

            else:
                file.write(ipv4_result + "\n")
                file.close()
        
        else:
            file_name = self.path + "ipv4.txt"

            ipv4_result = self.GetIpv4Address()

            if ipv4_result == "Error":

                return ""
        
            try:
                file = open(file_name, "w")

            except PermissionError as PE:
                print("Error: " + str(PE))

                return ""

            else:
                file.write(ipv4_result + "\n")
                file.close()
        
        return "Success"
               
        
def main() -> str:
    print("Tip: Enter \".\" for current directory")

    print("Enter the path of where the file will be stored: ", end="")

    Ipv4_Path = input()
    Ipv4_Path = Ipv4_Path.strip()

    if Ipv4_Path == "":
        print("[-] You didn't supply any input.")

        exit()

    if not Ipv4_Path == ".":
        if os.path.exists(Ipv4_Path) == True:
            pass
        else:
            print("[!] Path " + Ipv4_Path + " doesn't exist.")

            exit()

    if not Ipv4_Path.endswith("/"):
        Ipv4_Path = Ipv4_Path + "/"
    

    if Ipv4_Path == ".":
        ipv4_Obj = Ipv4AddressManager(Ipv4_Path, ".")

        if ipv4_Obj.Store_Ipv4() == "Success":
            print("[+] File created on your local directory.")

    else:
        ipv4_Obj = Ipv4AddressManager(Ipv4_Path, "blah")

        if ipv4_Obj.Store_Ipv4() == "Success":
            print("[+] File created on " + Ipv4_Path + " directory.")
    
    return "Success"

if __name__ == "__main__":
    main()
