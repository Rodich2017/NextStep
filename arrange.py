import os
import re

def take(dat):
    if (not os.path.isfile( dat )) or (not os.path.exists( dat )):
        print( "File not found!" )
        exit()
    else:
        # create new file name
        newfn, tail = str(os.path.basename(dat)).split('.')
        outdat = os.path.join(os.path.dirname(dat)) + "\\" +  newfn+"new."+tail

        try:
            # open file in read mode and save it in another
            with open( dat, "r", encoding="ANSI" ) as infile:
              with open( outdat, 'w' ) as outfile:
                line=infile.readline()
                cnt=1
                while line:
                    line = infile.readline ( )
                    cnt = 1
                    while line:
                        print ( "Line {}: {}".format ( cnt, line.strip ( ) ) )
                        line = infile.readline ( )
                        cnt += 1

                        a = len(line.split())
                        print(str(a))
                        if a == 11:
                            line_ckeck = re.match ( "\"\d", line )
                            if line_ckeck:
                                print ( str ( cnt ), " nameren " )
                                outfile.write ( line )
                        elif a == 13:
                            # da razfasovam masiva i da vzema 1-6 i 9-10 element
                            line_ckeck = re.match ( "\"\d", line )
                            if line_ckeck:
                                print ( str ( cnt ), " nameren " )
                                outfile.write ( line )
                        else:
                            continue
                    outfile.close ( )
                infile.close ( )

        except ValueError:
            print( ValueError.__name__ )
        except OSError as e:
            return e.errno
        else:
            return True
        finally:
            infile.close()


