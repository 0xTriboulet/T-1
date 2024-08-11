#include "intelligence.h"

int main(){
    
    DWORD process_count    = 0x0;
    DWORD user_count       = 0x0;
	float process_per_user = 0.0f;
    
    GetProcessCountViaSnapShot(&process_count);
    GetUniqueUserCountViaSnapshot(&user_count);
	
	process_per_user = process_count / user_count;
    
    PRINT("[i] Process Count        : %ld\n", process_count   );
    PRINT("[i] Process Count / User : %.2f\n" , process_per_user);
    PRINT("[i] Users Count          : %ld\n", user_count      );
	
	if(VmDetection(process_per_user)){
		
		// TODO: ShellcodeDetonation
		PRINT("[i] Executing shellcode!\n");
		
	}else{
		
		// TODO: SelfDelete
		PRINT("[i] Self-deleting!\n");
		
	}
	
    return 0;
}
