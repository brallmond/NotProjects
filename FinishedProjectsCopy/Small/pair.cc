#include <iostream>
#include <vector>

int main() {

  // initialize your container of pairs
  std::vector<std::pair<int,int>> vecPairs;

  // fill it with pairs
  vecPairs.push_back(std::make_pair(1,2));
  vecPairs.push_back(std::make_pair(2,3));
  vecPairs.push_back(std::make_pair(3,4));

  // container looks like
  // vecPairs = [(1,2),(2,3),(3,4)]
  
  // just get the front pair
  std::pair<int,int> frontPair = vecPairs.front();
  // could have used at(0) instead of front()

  // std::cout << frontPair << std::endl;
  // above statement gives compilation errors
  // so instead do

  std::cout << frontPair.first << std::endl;
  std::cout << frontPair.second << std::endl;

  // output is
  // 1
  // 2

  return 0;
}
