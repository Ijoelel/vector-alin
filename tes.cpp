#include <iostream>
using namespace std;

int main(){

	system("pwsh -Command \"$path = [Environment]::GetEnvironmentVariable(\'PATH\', \'Machine\'); echo $path ; $poppler_path = \'C:/poppler/Library/bin\'; echo $poppler_path ; [Environment]::SetEnvironmentVariable(\'Path\', \\\"$path;$poppler_path\\\", \'Machine\')\"");
	system("pip install Pillow");

	return 0;
}