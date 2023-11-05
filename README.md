
# SMS Simulation Exercise

This project simulates the process of sending a large number of SMS alerts, similar to an emergency alert service. 


## Components

### 1. **Producer**

The `Producer` class is responsible for generating a specified number of messages with random phone numbers and content. Each message is then added to a shared and synchronized message queue.

**Source File**     -> **src/Producer.py**

**Functionality**:
- Generates random 10-digit phone numbers.
- Generates random messages with up to 100 characters.
- Adds generated messages to a shared queue.

### 2. **Sender**

The `Sender` class simulates the process of sending messages. It picks messages from the shared queue and simulates sending them by waiting for a random period of time.

**Source File**     -> **src/Sender.py**

**Functionality**:
- Picks messages from the shared queue.
- Simulates message sending with a configurable failure rate.
- Updates the message store with the status of sent and failed messages.

### 3. **ProgressMonitor**

The `ProgressMonitor` class monitors and displays the progress of the message sending simulation at regular intervals.

**Source File**     -> **src/ProgressMonitor.py**

**Functionality**:
- Displays the number of messages sent, failed, and the average time per message.
- Updates the display at a configurable interval.

## Prerequisites

- **Python**: Ensure that you have Python 3.x installed on your system. 

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-repo-url.git
    cd your-repo-directory
    ```


## How to Run

### Running the Simulation

1. Navigate to the project directory in your terminal or command prompt.
2. Run the main simulation script using the following command:
    ```sh
    python main.py
    ```
### Follow the prompts to configure the simulation parameters

Number of messages   
No of senders   
Average processing time of senders  
Failure rate of senders  
Refresh rate of monitor

### Running Tests

#### Running Producer Tests
```sh
python Producer_test.py
```

#### Running Sender Tests
```sh
python Sender_test.py
```

#### Running ProgressMonitor Tests
```sh
python ProgressMonitor_test.py
```

## Expected Output

During the simulation, you should see output indicating the progress of the message sending, including the number of messages sent, the number of messages failed, and the average processing time per message.

