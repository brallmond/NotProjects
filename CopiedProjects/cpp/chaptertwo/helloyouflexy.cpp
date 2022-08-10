#include <iostream>
#include <string>

//libraries
using std::cin;		using std::cout;
using std::endl;	using std::string;

int main()
{
	//get name
	cout << "Please enter your first name: ";

	//read name
	string name;
	cin >> name;

	//number of blanks on left or right of greeting
	int sidepad = 0;
	cout << "How much space between your name and the left and right of the frame? (0,1,2,3,4,5,...) ";
	cin >> sidepad;
	//number of blanks above and below greeting
	int uplopad = 2;
	cout << "How much space between your name and the top and bottom of the frame? (0,1,2,3,4,5,...) ";
	cin >> uplopad;

	//build greeting
	const string spaceside(sidepad, ' ');
	const string greeting = spaceside + "Hello, " + name + "!" + spaceside;
	const string spacefull(greeting.size(), ' ');

	//number of rows and cols w pad and greeting info
	const int rows = uplopad*2 + 3;
	const string::size_type cols = greeting.size() + 2;

	//blank line to separate name input from framed output
	cout << endl;

	//write rows rows of output
	//invariant: we have written r rows so far
	for(int r = 0; r!=rows; ++r){
		string::size_type c = 0;

		//invariant: we have written c characters so far in the current row
		while(c!=cols){
			//is it time to write the greeting?
			if (r==uplopad + 1 && c == 1) {
				cout << greeting;
				c += greeting.size();
			}
			else{//are we on the border?
				if(r==0||r==rows-1||c==0||c==cols-1) {cout << "*"; ++c;}
				else{cout << spacefull; c += greeting.size();}
			}
		}
		cout << endl;
	}
	return 0;
}
