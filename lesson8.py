def divider():
    while True:
        nums=input('enter 2 digits(format: x y ):')
        (x,y)=nums.split()
        try:
            x = float(x)
            y = float(y)
            print(x/y)
        except ZeroDivisionError:
            print('Try again without zero')
        except ValueError:
            print('Try again without letters')
        except:
            print('something wrong')
            raise

def read_data(filename):
    lines = []
    infile = None
    try:
        infile = open(filename, encoding="utf8")
        for line in infile:
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if infile is not None:
            infile.close()
    return lines

read_data('age.txt')
