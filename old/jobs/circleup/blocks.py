def build_blocks(n):
    blocks = [[i] for i in range(0,n)]
    return blocks

def generate_lookup(n):
    lookup = {i: i for i in range(0,n)}
    return lookup

def move_block(pos, blocks, lookup):
    move = pos[0]
    onto = pos[1]
    #The current location of the block to move
    curr_loc = lookup[move]
    dest_loc = lookup[onto]
    if curr_loc == dest_loc:
        return blocks, lookup

    blocks, lookup = clear_blocks(blocks, lookup, curr_loc, move)
    blocks[curr_loc].remove(move)
    blocks, lookup = clear_blocks(blocks, lookup, dest_loc, onto)
    blocks[dest_loc].append(move)

    #Set the the location of the new block in the lookup table
    lookup[move] = lookup[onto]
    return blocks, lookup

def clear_blocks(blocks, lookup, location, stop):
    #Go through the block list backwards
    for block in blocks[location][::-1]:
        #if arrived at the move or onto block return
        if block == stop:
            return blocks, lookup
        #clearing the block from the location
        blocks[location].remove(block)
        #moving the block to its original index
        blocks[block].append(block)
        #setting the lookup value to its original value
        lookup[block] = block
    return blocks, lookup

def print_blocks(blocks):
    #for block in blocks:
    #    print block,
    print blocks

def usage():
    print 'Usage: MOVE X ONTO Y. ex: MOVE 4 ONTO 1\n'
    print 'Enter a command or press q or Q to quit\n'

def run():
    num_blocks = int(raw_input('Please enter the amount of blocks:\n'))
    blocks = build_blocks(num_blocks)
    lookup = generate_lookup(num_blocks)

    usage()
    while True:
        args = raw_input('COMMAND>>> ').split()
        if args[0].lower() == 'q':
            print 'Exiting...\n'
            return
        if len(args) != 4:
            print 'Invalid argument length\n'
            usage()
        elif args[0] != 'MOVE' and args[2] != 'ONTO':
            print 'Invalid Operations\n'
            usage()
        elif args[1] == args[3]:
            print 'Invalid positions entered\n'
            usage()
        elif not args[1].isdigit() and not args[3].isdigit():
            print 'Positions must be digits'
            usage()
        elif int(args[1]) > num_blocks-1 or int(args[3]) > num_blocks-1:
            print 'Position exceeds size of block table'
            usage()
        else:
            pos = int(args[1]), int(args[3])
            blocks, lookup = move_block(pos, blocks, lookup)
            print_blocks(blocks)

if __name__ == "__main__":
    run()
