#include <iostream>

void worry(){
  std::cout << ":( :( :(" << std::endl;
}

int main(){

bool problem = false;
bool thinking = true;

while(thinking){
  if (problem){ worry(); }
  else{ worry(); }
  }
return 0;
}
