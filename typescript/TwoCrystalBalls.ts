// given two crystal balls, and a building with n floors, find the exact floor where the ball start to break

export default function two_crystal_balls(breaks: boolean[]): number {
  // The big O of this is supposed to be O(sqrt n)
  let breaks_sqrt = Math.floor(Math.sqrt(breaks.length));
  let step = 0;

  // find where the first balls break
  for (; step < breaks.length; step += breaks_sqrt) {
    if (breaks[step]) {
      break;
    }
  }

  // go back last step before it brokr
  step -= breaks_sqrt;

  // let's break that second ball babe!
  for (let i = step; i < step + breaks_sqrt; i++) {
    if (breaks[i]) {
      return i;
    }
  }
  return -1
}
