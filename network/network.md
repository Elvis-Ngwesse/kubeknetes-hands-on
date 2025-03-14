
## Layer 7: Application Layer ##
This is the topmost layer of the OSI model. It's the layer where end-user applications interact with the network. It provides network services directly to end-users or applications
Web Browsing (HTTP/HTTPS): When you open a browser and type in a URL (e.g., https://www.example.com), the browser (a user application) uses the Application layer to send the request over the network. The application layer handles things like HTTP headers, URLs, etc.

## Layer 4: Transport Layer ##
The Transport layer ensures reliable data transfer between two devices and handles error detection, correction, and flow control.
TCP (Transmission Control Protocol): When you're sending data over the network, TCP breaks it into smaller packets, sends them to the destination, and ensures they arrive in order, and if not, it requests retransmission of missing packets.
UDP (User Datagram Protocol): For real-time applications like streaming, you might use UDP, where data is sent without the overhead of ensuring delivery, allowing faster communication at the cost of potential data loss.

## Layer 3: Internet Layer ## 
The Internet layer is responsible for logical addressing and routing, enabling communication between different networks.
IP Addressing: Every device on the internet or a network is assigned an IP address (like 192.168.1.1). When you send a request to a website, this layer ensures the data is directed to the correct device by using the destination IP address.

## Layer 3: Network Layer ##
The Network layer is a lower layer that deals with packet forwarding and routing across different networks. This layer is responsible for packet delivery from the source host to the destination host.
Routing: If you're using a router to connect to the internet, the router uses the Network layer to determine how to forward the packets to the destination IP.

## Layer 2: Data Link Layer ##
The Data Link layer is responsible for the reliable transfer of data across a physical link. It manages the physical addressing (MAC addresses), error detection, and frame synchronization. It ensures that data is transferred without errors between two devices within the same network or over a direct link.
Wi-Fi (IEEE 802.11): Wireless networks also use the Data Link layer to manage communication between devices and the access point.

## Layer 1: Physical Layer ##
The Physical layer is the lowest layer in the OSI model. It deals with the actual physical connection between devices. This layer is responsible for transmitting raw bits (0s and 1s) over a physical medium like cables, radio waves, or fiber optics.
Wi-Fi Signals: For wireless communication, the Physical layer handles the radio frequencies used by Wi-Fi networks.