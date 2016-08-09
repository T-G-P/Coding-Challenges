def string_vis(string):
    '''1. For some input string, for example "Peter Piper picked a peck of pickled peppers.",
    determine the character frequencies and display a simple visualization.

    ( e: ********

    p: *******

    ....

    )
    '''

    from collections import Counter
    letter_dict = dict(Counter(string))
    for letter, count in letter_dict.iteritems():
        visual = '*' * count
        print '%s: %s' % (letter, visual)

def gen_party_hat(num):
    '''2. Given a number, generate a party hat that many lines tall.

    ie. 5

      *
     ***

    *****
    '''

    num_lines = int(num) * 2 - 1

    for i in range(1,num_lines+2,2):
        spaces = ' ' * ((num_lines-i+1)/2)
        stars = '*' * i
        print spaces + stars

def clock_angle(hourmin):
    '''3.  Given the time on a digital clock in hours, minutes, and seconds (i.e. 01:52:30), figure out
    the angle between the hour and minute hands.#clockhands in python
    '''

    hours = int(hourmin[:2])
    minutes = int(hourmin[-2:])
    print hours,minutes

    minute_deg = minutes * 6
    hour_deg = (float(minutes)/60 + hours) * 15
    print float(minutes)/60
    print minute_deg,hour_deg

    degree_diff = abs(hour_deg - minute_deg)
    print 'The angle difference between the hour and minute hands is: %s degrees' % degree_diff

if __name__=="__main__":
    print '\nstring_vis(\'Peter Piper picked a peck of pickled peppers.\')\n'
    string_vis('Peter Piper picked a peck of pickled peppers.')
    print '\ngen_party_hat(15)\n'
    gen_party_hat(15)
    print '\nclock_angle(\'06:06:06\')\n'
    clock_angle('06:06:06')

    test_string = raw_input('Enter a string and see it\'s visual output\n')
    string_vis(test_string)

    test_num = raw_input('Enter a number and see it\'s party hat\n')
    gen_party_hat(test_num)

    test_time = raw_input('Enter a time in in (hour:min:seconds) format\n')
    clock_angle(test_time)
