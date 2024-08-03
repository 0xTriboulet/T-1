#include "intelligence.h"

int main(){
    
    DWORD process_count = 0x0;
    DWORD user_count    = 0x0;
    
    GetProcessCountViaSnapShot(&process_count);
    GetUniqueUserCountViaSnapshot(&user_count);
    
    PRINT("[i] Process Count        : %ld\n", process_count);
    PRINT("[i] Process Count / User : %ld\n", process_count / user_count);
    PRINT("[i] Users Count          : %ld\n", user_count   );
    
    return 0;
}
