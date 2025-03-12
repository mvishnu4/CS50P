def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        if plate[0].isalpha and plate[1].isalpha:
            for i in range(len(plate) - 1):
                if plate[i] == "." or plate[i] == " " or plate[i] == "?" or plate[i] == "!" or plate[i] == "," or plate[i] == ";" or plate[i] == ":":
                    return False
                    break
                if plate[i].isdigit() and not(plate[i+1].isdigit):
                    return False
                    break
                elif plate[i] == "0" and plate[i+1] != "0":
                    return False
                    break
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()