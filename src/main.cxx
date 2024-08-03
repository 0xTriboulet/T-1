#include "intelligence.h"

int main(){
    
    DWORD process_count = 0x0;
    DWORD user_count    = 0x0;
    
    GetProcessCountViaSnapShot(&process_count);
    GetUniqueUserCountViaSnapshot(&user_count);
    
    PRINT("[i] Processes: %ld\n", process_count);
    PRINT("[i] Users    : %ld\n", user_count   );
    
    return 0;
}
