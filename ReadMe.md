# **AI-Assisted Developer Tools Setup and Evaluation Guide**

Welcome to the AI-Assisted Developer Tools Evaluation! This guide will walk you through the setup of **Codium**, **GitHub Copilot**, and **Tabnine**. It also explains how to rotate between tools while completing the three evaluation projects.

---

## **1. Tool Setup Instructions**

Detailed instructions are provided by each individual supplier. Rather than re-inventing the wheel, the links are given below. If any setup issues arise, please speak up and troubleshooting support will be immediately provided. 

### **1.1 Codium**
- **Setup**:
  - Follow the installation guide here: [Codium Installation](https://docs.codeium.com/extensions/getting-started).
  - Install the extension for your IDE (e.g., VS Code).
  - **Sign Up**: Use your company email to register an account.
  - After registration, Codium will provide access to the Pro Subscription.
  
### **1.2 GitHub Copilot**
- **Setup**:
  - Follow the quickstart guide here: [GitHub Copilot Setup](https://docs.github.com/en/copilot/quickstart).
  - Install the extension for your IDE.
  - GitHub CoPilot has a free tier, that will be sufficient for this test. The only difference between the pro and free tier is the number of calls to the API. 

### **1.3 Tabnine**
- **Setup**:
  - Follow the installation guide here: [Tabnine Installation](https://docs.tabnine.com/main/getting-started/misc/client-setup-saas/vs-code).
  - Install the extension for your IDE.
  - Use a free Tabnine account for this evaluation.

---

## **2. Rotating Between Tools**

You will evaluate the tools in the following order:  
**Codium → GitHub Copilot → Tabnine** (rolling order).  

- Start with **Codium** if your last name begins with **A–H**.
- Start with **GitHub Copilot** if your last name begins with **I–R**.
- Start with **Tabnine** if your last name begins with **S–Z**.

After completing a task, **disable the current extension**, enable the next tool in the sequence, and restart VS Code to ensure clean operation.

To disable the tool, look for the tool's name in the bottom right-hand corner of the window. Click it, then click disable extension. 

---

## **3. Projects**

Each project focuses on specific development tasks to test the tools.

### **3.1 Project 1: Monty Hall Problem**
**Focus**: Basic implementation and getting familiar with the tools.  
- **Task**: Complete a Python scaffold for the Monty Hall simulation.
- Use **autocomplete** and **chat** features to:
  - Implement methods.
  - Clarify questions about the problem.
- Test the implementation using the provided test suite.

**What to Look For**:
- Accuracy and speed of autocomplete suggestions.
- How effectively the chat explains concepts or generates code snippets.

---

### **3.2 Project 2: Bank Account Simulator**
**Focus**: Code creation, testing, and refactoring.  
- **Task**:
  - Extend the base `BankAccount` class to implement new account types.
  - Generate unit tests for functionality.
  - Refactor the base class for simplicity.

**What to Look For**:
- How well the tool generates new classes and test cases.
- Effectiveness in refactoring overly complex code.

---

### **3.3 Project 3: Blackjack Challenge**
**Focus**: Bug fixing and testing enhancements.  
- **Task**:
  - Identify and fix introduced bugs in the PyDealer library.
  - Expand the testing suite and implement missing functionality like the `cut()` method.

**What to Look For**:
- AI’s ability to identify, explain, and resolve tricky bugs.
- How well the tool generates tests to validate fixes.

---

## **4. Switching Between Tools**

1. Complete a project task with the current tool (e.g., Codium).
2. **Disable the extension** in VS Code:
   - Go to the Extensions tab, find the tool, and click **Disable**.
3. **Enable the next tool** in the sequence (GitHub Copilot → Tabnine → Codium).
4. Restart VS Code to ensure clean operation.

---

## **5. Evaluation Criteria**

Evaluate each tool based on the following capabilities:

### **Autocomplete**
- **Autocomplete Performance**: Accuracy and speed of suggestions.
- **In-line Code Completion**: Quality of in-line (Fill-In-the-Middle) completions.

### **Chat**
- **In-IDE Integrated Chat**: Usefulness of the chat tool for clarifying and generating solutions.
- **Documentation Generation**: Quality of generated docstrings and explanations.
- **Code Explanation**: Effectiveness in explaining snippets or errors.
- **Error Correction**: Ability to identify and correct issues.
- **Unit Test Generation**: Quality of generated test cases.

### **Command**
- **Generate New Components**: Effectiveness in creating new classes, functions, or interfaces.
- **Refactor Functions**: Quality and accuracy of refactored code.
- **Resolve Multi-Line Bugs**: Ability to diagnose and resolve tricky, multi-line issues.

### **Context Awareness**
- **Context Pinning**: Effectiveness in understanding project-specific context for better suggestions.

---

## **6. Time Management**

- Spend **no more than 40 minutes per project** using each tool.
- If you cannot complete the task in 40 minutes, move on and document progress.
- Rotate to the next tool as described.

---

## **7. Feedback**

Record your scores for each tool in the provided spreadsheet:
- Compare tools side-by-side.
- Allocate 100 points across all categories to indicate their importance to you.

---

By following these instructions, you’ll gain a comprehensive understanding of how Codium, GitHub Copilot, and Tabnine perform across real-world development scenarios. Happy coding and good luck!
