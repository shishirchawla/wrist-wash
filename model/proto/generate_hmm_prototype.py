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

    ## ALL FORWARD MODEL
#    # first row
#    prob = 1.0/(states-1)
#    hmmproto.write('  0.0')
#    for j in range(0, states-2):
#      hmmproto.write(" {:.3f}".format(prob))
#    last_prob = 1.0-(float("{:.3f}".format(prob))*(states-2))
#    hmmproto.write(" {:.3f}".format(last_prob))
#    hmmproto.write('\n')
#    # middle rows
#    for i in range(0, states-2):
#      hmmproto.write(' ')
#      prob = 1.0/(states-1-i)
#      for j in range(0, i+1):
#        hmmproto.write(' 0.0')
#      for j in range(0, states-1-i-1):
#        hmmproto.write(" {:.3f}".format(prob))
#      last_prob = 1.0-(float("{:.3f}".format(prob))*(states-1-i-1))
#      hmmproto.write(" {:.3f}".format(last_prob))
#      hmmproto.write('\n')
#    # last row
#    hmmproto.write(' ')
#    for i in range(0, states):
#      hmmproto.write(' 0.0')
#    hmmproto.write('\n')

    ## N FORWARD MODEL
    n = 2
    # first row
    prob = 1.0/(n)
    hmmproto.write('  0.0')
    for j in range(0, n-1):
      hmmproto.write(" {:.3f}".format(prob))
    last_prob = 1.0-(float("{:.3f}".format(prob))*(n-1))
    hmmproto.write(" {:.3f}".format(last_prob))
    for j in range(0, states-n-1):
      hmmproto.write(' 0.0')
    hmmproto.write('\n')
    # middle rows
    for i in range(0, states-2):
      hmmproto.write(' ')
      prob = 1.0/(states-1-i)
      for j in range(0, i+1):
        hmmproto.write(' 0.0')
      if i+n < states:
        prob = 1.0/(n)
        for j in range(0, n-1):
          hmmproto.write(" {:.3f}".format(prob))
        last_prob = 1.0-(float("{:.3f}".format(prob))*(n-1))
        hmmproto.write(" {:.3f}".format(last_prob))
        for j in range(0, states-n-1-i):
          hmmproto.write(' 0.0')
      else:
        prob = 1.0/(states-i-1)
        for j in range(0, states-i-1-1):
          hmmproto.write(" {:.3f}".format(prob))
        last_prob = 1.0-(float("{:.3f}".format(prob))*(states-i-1-1))
        hmmproto.write(" {:.3f}".format(last_prob))
      hmmproto.write('\n')
    # last row
    hmmproto.write(' ')
    for i in range(0, states):
      hmmproto.write(' 0.0')
    hmmproto.write('\n')

    ## BAKIS MODEL
#    # first row
#    hmmproto.write('  0.0 0.5 0.5')
#    for i in range(0, states-3):
#      hmmproto.write(' 0.0')
#    hmmproto.write('\n')
#    # middle rows
#    if (states - 3) > 0:
#      for i in range(0, states-3):
#        hmmproto.write(' ')
#        for j in range(0, i+1):
#          hmmproto.write(' 0.0')
#        hmmproto.write(' 0.33 0.33 0.34')
#        for k in range(0, states-(i+3+1)):
#          hmmproto.write(' 0.0')
#        hmmproto.write('\n')
#    # second last row
#    hmmproto.write(' ')
#    for i in range(0, states-2):
#      hmmproto.write(' 0.0')
#    hmmproto.write(' 0.5 0.5\n')
#    # last row
#    hmmproto.write(' ')
#    for i in range(0, states):
#      hmmproto.write(' 0.0')
#    hmmproto.write('\n')

    hmmproto.write('<EndHMM>\n')

if __name__ == '__main__':
  main()
