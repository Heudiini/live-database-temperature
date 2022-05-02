from serial import *
import time
import sqlite3
import json

JSON= "data.json"

def Tapahtuma(data):

    if len(data) >= 2:  
        try:
            conn = sqlite3.connect('tietokanta2.db')
      
            with open(JSON) as tuonti:
                    json_data = json.load(tuonti)
                
        except json.decoder.JSONDecodeError:
                json_data = {} 
                
        except FileNotFoundError:
                json_data = {} 
                
                open(JSON, 'a').close() 
                os.chmod(JSON, 0o755) 
            
        #json_data['aika'] = int(time.time())
        json_data["asteet"] = int(data[:])
          
        try:
                with open(JSON, 'w') as outfile:
                    json.dump(json_data, outfile)
        except Exception:
                print('Ei pysty kirjoittamaan')   
  
        except Exception:
            print("tietokantaa ei avattu")
            sys.exit()
            
        c = conn.cursor()
        aika = int(time.time())
        #print(aika)
        asteet = int(data[:])
        print(asteet)
        
        c.execute("INSERT INTO temperature VALUES (?, ?)", (aika,asteet))
        conn.commit()
        conn.close()
        ###########################
    
    
def main():
    # Yritetään luoda sarjaportti
    try:
        microbit = Serial(port='/dev/ttyACM0', baudrate=115200, timeout=2)
    except Exception:
        print("tarkista portti")
    while True:
        try:
            Tapahtuma(microbit.readline().decode()) # luetaan rivi
        except KeyboardInterrupt:
            print("keskeytetään")
            sys.exit()
            
            



if __name__ == "__main__":
    main()
    