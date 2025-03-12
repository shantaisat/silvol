# silvol


## Overview
Silvol is a platform built with Django that connects tech-savvy volunteers with elderly individuals to help them overcome tech-related challenges. The application provides full CRUD functionality, allowing volunteers to create, read, update, and delete tech support appointments. Silvol empowers volunteers to gain experience and give back to the community by assisting elderly users with popular technologies like Zoom, WhatsApp, Alexa, Google services, Skype, and more. The platform bridges the digital divide, enabling elderly users to learn how to use technology to stay connected and combat loneliness, while fostering a sense of community and support.

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/username/project/kanban)
- **Wireframes:**
  - [Wireframe Designs](https://linktowireframes.com)
  - Wireframes were designed to ensure clarity, intuitive navigation, and compatibility with assistive technologies. High-contrast colours and alt text for images were used to maximise accessibility.
- **Design Rationale:**
- The layout of Silvol prioritises simplicity and user-friendliness, ensuring an intuitive   experience for both volunteers and elderly users. The responsive design, built with Django and styled using Bootstrap 5, adapts seamlessly across various devices, making the platform accessible from desktops, tablets, and smartphones.

- The colour scheme is carefully selected to meet WCAG guidelines for contrast, providing high visibility and clarity for all users, including those with visual impairments. The typography is designed with legibility in mind, using accessible fonts to enhance readability.

- Accessibility features are integral to the platform, including keyboard navigation, clear visual cues, and support for screen readers. These considerations ensure that Silvol is usable by individuals with diverse needs, enhancing its inclusivity and overall effectiveness.

- **Reasoning For Any Final Changes:**
  - Based on user feedback, adjustments were made to enhance usability, such as reordering navigation elements for better flow and refining accessibility features. These changes improve the inclusivity of the application.

## Key Features
Volunteer & Elderly User Profiles: Create, view, update, and delete profiles for both volunteers and elderly users, allowing detailed information such as skills, availability, and tech needs.

-**Appointment Management**: Volunteers can create, view, update, and delete tech support appointments, helping elderly users with their tech-related challenges.

-**User Authentication**: Secure login/logout functionality for both volunteers and elderly users, ensuring safe access and privacy for all platform members.

-**Inclusivity Features:**
Accessibility features include ARIA labels and 'alt' attributes on images, ensuring that the platform is usable with screen readers. Keyboard navigation is supported for easy navigation by users with disabilities.

## Deployment
- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Clone the repository
  2. Set up the Heroku environment with a PostgreSQL database.
  3. Configure environment variables for sensitive data (e.g., secret keys).
  4. Deploy using Heroku Git or GitHub integration.
- **Verification and Validation:**
  - Tested the deployed application against the development environment for consistent functionality and design.
  - Verified accessibility using tools such as Lighthouse and manual testing.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - DEBUG mode is disabled in the production environment to enhance security.

## AI Implementation and Orchestration

### Use Cases and Reflections:

**Throughout this project, I relied on GitHub Copilot to streamline development and testing. This was my first time using AI tools so extensively, and it became an invaluable collaborator during the process.

- **Code Creation:** 
  - Reflection: Initially, I was hesitant about how much I could rely on Copilot, but I quickly saw its value in generating boilerplate code, like Django models and CRUD views. Using reverse and multi-step prompts gave me the confidence to explore alternative approaches, and it even taught me new techniques I hadn’t considered before. For instance, it suggested cleaner, more Pythonic ways to handle database queries that saved me time and effort.
  - Highlight: The iterative back-and-forth with Copilot felt like having a knowledgeable pair programmer by my side. This collaboration made me more thoughtful about how I structured my prompts, as clearer questions led to better answers.

- **Debugging:** 
  - Reflection: Debugging with Copilot was a learning experience in itself. It didn’t just find errors; it often suggested solutions that highlighted gaps in my understanding. I appreciated how it encouraged me to simplify complex logic, making the code easier to maintain and more accessible to anyone who might work on it in the future.

- **Performance and UX Optimization:** 
  - Reflection: One of my proudest moments came when I used Copilot to refine the Bootstrap styling. I wasn’t very confident in front-end design, but the AI helped bridge that gap. It suggested small, impactful changes, like improving button alignment and tweaking breakpoints, that made the application feel polished and professional. These adjustments also ensured that the app was truly responsive, which was a priority for me.

- **Automated Unit Testing: (If undertaken)**
  - Reflection: Writing unit tests has always been a challenging aspect of development for me, but Copilot turned it into a manageable task. I used question-and-answer and multi-step prompts to generate a solid starting point for my test cases, which I could then refine to align with the project’s requirements. Seeing it anticipate edge cases—like invalid user input—made me more aware of the importance of writing comprehensive tests. This process deepened my understanding of Django’s testing framework and made me more confident in my ability to create robust applications.

### Overall Impact:
Working with Copilot transformed my workflow. It allowed me to focus on higher-level decisions while handling repetitive tasks efficiently. However, it wasn’t always perfect—some suggestions required significant tweaking to fit my specific needs. Those moments were valuable reminders that the AI wasn’t a replacement for my skills but a tool to enhance them. 

Looking back, I feel this experience not only improved my technical abilities but also my problem-solving skills. It pushed me to articulate my ideas clearly (both to the AI and myself) and made me more mindful of inclusivity and accessibility in software design. Above all, it taught me the importance of embracing new technologies as partners in the creative process.


## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** Windows 11 (Chrome, Edge), macOS (Safari), Android, iOS.
  - **Assistive Technologies:** Tested using Lighthouse in the Developer Tools.
  - **Features Tested:** CRUD operations, user authentication, responsive design, and accessibility features.
  - **Results:** All critical features, including accessibility checks, worked as expected.
- **Automated Testing:(If undertaken)**
  - Tools Used: Django TestCase, GitHub Copilot.
  - Features Covered: CRUD operations, user authentication, and accessibility compliance.
  - Adjustments Made: Additional manual modifications to ensure comprehensive test coverage and inclusivity.

## Future Enhancements
- Add a notification feature for upcoming events and deadlines.
- Build multilingual support for non-English-speaking users.
- Learn how to build or integrate analytics for tracking user engagement with notices.