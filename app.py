import sys
import main
import auth

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == 'code':
            auth.getcodeurl()
        elif cmd == 'token':
            auth.gettoken(sys.argv[2])
        else:
            print 'invalid command: ' + cmd
    else:
        bot = main.Bot()
        bot.run()
