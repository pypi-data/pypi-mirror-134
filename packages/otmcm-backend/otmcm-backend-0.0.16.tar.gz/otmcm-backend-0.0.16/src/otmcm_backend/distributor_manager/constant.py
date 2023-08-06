class DistributorManagerConstant:
    class Default:
        class PublicEndpoint:
            # Avaialble in network
            PORT = 1997
            ADDRESS = f"tcp://*:{PORT}"
    
        class IPCEndpoint:
            # Available Interprocess address
            ADDRESS = f"ipc:///tmp/otmcm_backend/distributor_manager"
            
