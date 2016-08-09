class BlocksWorld(object):

    def __init__(self, num_blocks):
        self.blocks = self.build_blocks(num_blocks)
        self.lookup = self.generate_lookup(num_blocks)

    def build_blocks(self,n):
        blocks = [[i] for i in range(0,n)]
        return blocks

    def generate_lookup(self,n):
        lookup = {i: i for i in range(0,n)}
        return lookup

    def move_block(self, pos):
        move = pos[0]
        onto = pos[1]
        #The current location of the block to move
        move_loc = self.lookup[move]
        #Destination where block is moving to
        onto_loc = self.lookup[onto]
        if move_loc == onto_loc:
            print 'These blocks are stacked together already'
            return

        #Clearing both move/onto locations and moving the block
        self.clear_blocks(move_loc, move)
        self.blocks[move_loc].remove(move)
        self.clear_blocks(onto_loc, onto)
        self.blocks[onto_loc].append(move)

        #Set the the location of the new block in the lookup table
        self.lookup[move] = self.lookup[onto]

    def clear_blocks(self, location, stop):
        #Go through the block list backwards
        for block in self.blocks[location][::-1]:
            #if arrived at the move or onto block return
            if block == stop:
                return
            #clearing the block from the location
            self.blocks[location].remove(block)
            #moving the block to its original index
            self.blocks[block].append(block)
            #setting the lookup value to its original value
            self.lookup[block] = block

    def print_blocks(self):
        print self.blocks

    def usage(self):
        print '\nUsage: MOVE X ONTO Y. ex: MOVE 4 ONTO 1\n'
        print 'Enter a command or press q or Q to quit\n'
        print 'Type \'help\' for usage info'

    def run(self):
        self.usage()
        self.print_blocks()
        while True:
            args = raw_input('COMMAND>>> ').split()
            if args[0].lower() == 'q':
                print 'Exiting...\n'
                return
            if args[0].lower() == 'help':
                self.usage()
            elif len(args) != 4:
                print 'Invalid argument length\n'
                self.usage()
            elif args[0].lower() != 'move' and args[2].lower() != 'onto':
                print 'Invalid Operations\n'
                self.usage()
            elif args[1] == args[3]:
                print 'Invalid positions entered\n'
                self.usage()
            elif not args[1].isdigit() and not args[3].isdigit():
                print 'Positions must be digits'
                self.usage()
            elif int(args[1]) > num_blocks-1 or int(args[3]) > num_blocks-1:
                print 'Position exceeds size of block table'
                self.usage()
            else:
                #The position the block is moving to
                pos = int(args[1]), int(args[3])
                self.move_block(pos)
                self.print_blocks()

if __name__ == "__main__":
    num_blocks = int(raw_input('Please enter the amount of blocks:\n'))
    block_test = BlocksWorld(num_blocks)
    block_test.run()
