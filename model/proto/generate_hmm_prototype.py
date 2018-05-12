import sys

def main():
  if len(sys.argv) < 4:
    print 'provide all parameters - "#states #gausperstate #featurevectorlength"'
    exit(1)

  states = int(sys.argv[1])
  gausperstate = int(sys.argv[2])
  featurevectorlength = int(sys.argv[3])

  generate_hmm_prototype(states, gausperstate, featurevectorlength)

def generate_hmm_prototype(states, gausperstate, featurevectorlength):
  with open('hmmproto_'+str(states)+'_'+str(gausperstate)+'_'+str(featurevectorlength), 'w') as hmmproto:
    hmmproto.write('~o <VecSize> '+str(featurevectorlength)+' <MFCC>\n')
    hmmproto.write('~h "proto"\n')
    hmmproto.write('<BeginHMM>\n')
    hmmproto.write('  <NumStates> {}\n'.format(states))
    for i in range(0, states-2):
      hmmproto.write('  <State> '+str(i+2)+'\n')
      hmmproto.write('    <NumMixes> '+str(gausperstate)+'\n')

      for j in range(0, gausperstate):
        if j != gausperstate-1:
          hmmproto.write('    <Mixture> '+str(j+1)+' {:.3f}\n'.format(round(1.0/gausperstate, 3)))
        else:
          hmmproto.write('    <Mixture> '+str(j+1)+' {:.3f}\n'.format(1.0-round(1.0/gausperstate, 3)*(gausperstate-1)))

        hmmproto.write('      <Mean> {}\n'.format(featurevectorlength))
        hmmproto.write('        ')
        for k in range(0, featurevectorlength):
          hmmproto.write('0.0 ')
        hmmproto.write('\n')
        hmmproto.write('      <Variance> {}\n'.format(featurevectorlength))
        hmmproto.write('        ')
        for k in range(0, featurevectorlength):
          hmmproto.write('1.0 ')
        hmmproto.write('\n')

    hmmproto.write('  <TransP> {}\n'.format(states))

    # first row
    hmmproto.write('  0.0 0.5 0.5')
    for i in range(0, states-3):
      hmmproto.write(' 0.0')
    hmmproto.write('\n')
    # middle rows
    if (states - 3) > 0:
      for i in range(0, states-3):
        hmmproto.write(' ')
        for j in range(0, i+1):
          hmmproto.write(' 0.0')
        hmmproto.write(' 0.33 0.33 0.34')
        for k in range(0, states-(i+3+1)):
          hmmproto.write(' 0.0')
        hmmproto.write('\n')
    # second last row
    hmmproto.write(' ')
    for i in range(0, states-2):
      hmmproto.write(' 0.0')
    hmmproto.write(' 0.5 0.5\n')
    # last row
    hmmproto.write(' ')
    for i in range(0, states):
      hmmproto.write(' 0.0')
    hmmproto.write('\n')

    """
    if states == 3:
      hmmproto.write('  0.0 0.5 0.5\n  0.0 0.5 0.5\n  0.0 0.0 0.0\n')
    elif states == 4:
      hmmproto.write('  0.0 0.5 0.5 0.0\n  0.0 0.33 0.33 0.34\n  0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0\n')
    elif states == 5:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0\n  0.0 0.33 0.33 0.34 0\n  0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0\n')
    elif states == 7:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    elif states == 9:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    elif states == 11:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    elif states == 13:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    elif states == 15:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    elif states == 17:
      hmmproto.write('  0.0 0.5 0.5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n'  \
                     + '  0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34 0.0\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.33 0.33 0.34\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.5 0.5\n  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0\n')
    else:
      hmmproto.write('NOT SUPPORTED\n')
    """
    hmmproto.write('<EndHMM>\n')

if __name__ == '__main__':
  main()
