# Understanding HTTP, HTTPS, and SSL/TLS
*(A look under the hood of web security)*

## The Goal
This repository documents my architectural understanding of how secure web communication works. My goal here is to lay the theoretical foundations: understanding the *why* and *how* of these protocols, without getting tangled up in low-level implementations for now.

## HTTP vs. HTTPS (The simple explanation)

To understand the fundamental difference, imagine you want to send an important document to someone by mail:

*   **HTTP (The Postcard):** This is the base protocol. It works as if you were sending a traditional postcard. The message travels exposed (in "plain text"). The mail carrier, or anyone who intercepts that postcard along the way, can read everything you've written.
*   **HTTPS (The Safe):** This is the security layer. It works as if you put that same postcard inside a safe. The safe travels through the same postal system in plain sight of everyone, but because it is encrypted, only the final recipient has the key to open it.

<img width="2048" height="1316" alt="image" src="https://github.com/user-attachments/assets/37c57e3d-5ae0-4713-9ea9-bbd062cb4a9b" />

| Feature | HTTP (Hypertext Transfer Protocol) | HTTPS (HTTP Secure) |
| :--- | :--- | :--- |
| **Data format** | Plain text (Vulnerable to interception) | Encrypted text (Privacy in transit) |
| **Identity** | You don't know for sure who the receiver is | Uses Digital Certificates to ensure identity |
| **Main use** | Obsolete for any sensitive data | Mandatory standard on today's web |

---

## The guts of the system: The "Handshake"

HTTPS doesn't happen by magic. For your computer and the web server to create that secure tunnel, they have to agree on a process called the **Handshake**. This happens in a matter of milliseconds:

<img width="554" height="554" alt="image" src="https://github.com/user-attachments/assets/8809694a-9252-4cac-9a6a-bb08c75763df" />

1.  **The initial "Hello":** Your browser says: *"Hello, I want to talk securely. These are the encryption tools I know how to use."* The server replies: *"Hello, perfect. We will use this specific tool, and here is my Digital Certificate (my ID card) so you can verify that I am who I claim to be."*
2.  **The Validation (Asymmetric Cryptography):** Your browser checks that the certificate is real and issued by a trusted entity. If everything checks out, it uses the server's public key to send it a mathematical "secret".
3.  **The Tunnel (Symmetric Cryptography):** With that mathematical secret, both parties calculate a unique and temporary master key. From then on, they stop using public/private keys and only use that master key to encrypt everything they send to each other. It is a mixed system that makes communication ultra-secure and, at the same time, very fast.

> **💡 Technical note (SSL vs. TLS):** Historically, the technology that achieved this was called **SSL** (Secure Sockets Layer). Over the years it evolved, security flaws were fixed, and it was renamed **TLS** (Transport Layer Security). Although almost everyone still talks about "SSL Certificates" out of habit, today we all use TLS.

---

## Project Status and Next Steps

Currently, I consider that I have fulfilled my initial plan: I have a solid understanding of the architecture and mechanics behind these protocols.

I know this has a real technical impact (for example, implementing HTTPS on limited hardware or IoT projects requires extra memory and processing just to calculate the Handshake), but **I don't see the relevance of digging deeper at the code level or server configuration at this time**.

I leave this milestone documented as an assimilated technical foundation, keeping the door open to dive deeper in the future if scalability or project needs demand it.
