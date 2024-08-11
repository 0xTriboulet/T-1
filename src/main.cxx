#include "intelligence.h"

int main(){
    
    DWORD process_count    = 0x0;
    DWORD user_count       = 0x0;
	float process_per_user = 0.0f;
    
    GetProcessCountViaSnapShot(&process_count);
    GetUniqueUserCountViaSnapshot(&user_count);
	
	process_per_user = process_count / user_count;
    
    PRINT("[i] Process Count        : %ld\n", process_count);
    PRINT("[i] Process Count / User : %f\n" , process_per_user);
    PRINT("[i] Users Count          : %ld\n", user_count   );
	
	
    
    return 0;
}
