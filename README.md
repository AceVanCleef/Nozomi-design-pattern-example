# Nozomi Design Pattern Demo: Adaptive Protocol Parsing via Network Signatures

## Simulated Scenario & Case Study

### The Challenge
Siemens is developing a new edge device for power plants. To enable seamless interoperability, this device must analyze and understand network traffic from a variety of existing infrastructure. 

However, operators in modern power plants face a heterogeneous environment:
* **Multi-Vendor Environments:** Devices from different manufacturers run side-by-side.
* **Protocol Silos:** Each device communicates using its own distinct network protocol (e.g., Profibus, Modbus TCP, or generic binary streams).

### The Solution
To bridge this gap and facilitate cross-protocol communication, this project implements an adaptive **Protocol Parser**. By dynamically analyzing the binary signature (magic bytes) of incoming network streams, the system automatically detects the underlying protocol and spins up the correct parsing engine on the fly.


## Architectural Design & Patterns

To ensure maximum reliability and maintainability, the architecture decouples protocol detection from the actual parsing logic using two classic Gang of Four (GoF) design patterns:

1. **Strategy Pattern:** Every protocol has its own decoupled parsing engine (e.g., `ProfibusParser`, `ModbusParser`). They all implement a unified `ProtocolParser` interface. This allows the system to extend support for new protocols easily without changing existing code (Open-Closed Principle).
2. **Factory Method Pattern:** The `ParserFactory` acts as the brain. It evaluates the incoming raw binary stream via `can_parse()` and dynamically selects and instantiates the correct `ProtocolParser` strategy.

---

## Testing Strategy: The Integration Matrix

Rather than writing isolated, redundant unit tests for every single parser, this project introduces a **Parameterized Test Matrix** via `pytest`. 

This approach serves as a living specification:
* It maps input streams directly to their expected architectural behavior across all parsers simultaneously.
* It guarantees that specialized parsers never accidentally cross-fire on overlapping byte signatures.

To execute the test suite, run:
```bash
pytest
```

## Production Readiness & Next Steps (TBD)
This repository serves as an architectural proof-of-concept and demonstration of the commonly used `strategy pattern` and the `factory method pattern`. This repository does not go beyond the purpose of demonstration.

Though, to complete the test suite, expected error cases could be tested. They have been skipped since they go beyond the scope of demonstrating these design patterns.

## Setup & Validation

Ensure you have Python 3.14+ installed. Follow these steps to set up the environment and run the test suite:

### 1. Clone the Repository
```bash
git clone [Nozomi-design-pattern-example](ttps://github.com/AceVanCleef/Nozomi-design-pattern-example.git)
cd Nozomi-design-pattern-example
```

### 2. Set Up the Virtual Environment
Create a clean environment without automated pip packages to avoid Windows path/subprocess locking:
```bash
python -m venv .venv --without-pip
.venv\Scripts\Activate.ps1
python -m ensurepip --default-pip
```

### 3. Install Dependencies
``` Bash
pip install pytest
```

### 4. Execute the Test Suite
Run the automated test matrix to verify requirements, edge cases, and type guard clauses:
```Bash
pytest
```