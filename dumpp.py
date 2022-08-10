user.append(nmp)
        dumpp = open(save_file,'w')
        for bilal in user:
            uid = code+bilal
            dumpp.write(uid+' | '+'MALIK_RANDOM_DUMP'+'\n')
            print(uid+' | '+'MALIK_RANDOM_DUMP')
            time.sleep(0.05)
        dumpp.close()
        print("Dumping Done ")
        print(f"Your File Save As {save_file}")
    except Exception as e:
        print(e)