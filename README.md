# silvol
https://github.com/shantaisat/silvol



## Overview
Silvol is a platform built with Django that connects tech-savvy volunteers with elderly individuals to help them overcome tech-related challenges. The application provides full CRUD functionality, allowing volunteers to create, read, update, and delete tech support appointments. Silvol empowers volunteers to gain experience and give back to the community by assisting elderly users with popular technologies like Zoom, WhatsApp, Alexa, Google services, Skype, and more. The platform bridges the digital divide, enabling elderly users to learn how to use technology to stay connected and combat loneliness, while fostering a sense of community and support.

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/users/shantaisat/projects/8)
- **Wireframes:**
  - [Wireframe Designs](https://linktowireframes.com)
  - Wireframes were designed to ensure clarity, intuitive navigation, and compatibility with assistive technologies. High-contrast colours and alt text for images were used to maximise accessibility.
- **Design Rationale:**
- The layout of Silvol prioritises simplicity and user-friendliness, ensuring an intuitive   experience for both volunteers and elderly users. The responsive design, built with Django and styled using Bootstrap 5, adapts seamlessly across various devices, making the platform accessible from desktops, tablets, and smartphones.

- The colour scheme is carefully selected to meet WCAG guidelines for contrast, providing high visibility and clarity for all users, including those with visual impairments. The typography is designed with legibility in mind, using accessible fonts to enhance readability.

- Accessibility features are integral to the platform, including keyboard navigation, clear visual cues, and support for screen readers. These considerations ensure that Silvol is usable by individuals with diverse needs, enhancing its inclusivity and overall effectiveness.

 - **Reasoning For Any Final Changes:**
  - Based on user feedback, adjustments were made to enhance usability, such as reordering navigation elements for better flow and refining accessibility features. These changes improve the inclusivity of the application.-->

## Key Features
Volunteer & Elderly referral User Profiles: Create, view, update, and delete profiles for both volunteers and elderly users, allowing detailed information such as skills, availability, and tech needs.

The user journeys for referral users and volunteers are distinct but complementary. Referral users focus on finding and connecting with volunteers, while volunteers manage their availability and assist referral users. The platform's design ensures simplicity and inclusivity for both user types, with features tailored to their specific needs.

-**Availability Management**: Volunteers can create, view, update, and delete tech support availabilty, helping elderly users with their tech-related challenges.

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

Throughout this project, I leveraged multiple AI tools, including GitHub Copilot, ChatGPT, and Discord MidJourney, to streamline development, enhance creativity, and improve the overall user experience. Each tool played a unique role in shaping the platform.

## GitHub Copilot
- **Code Creation:** 
  - Reflection: GitHub Copilot was instrumental in generating boilerplate code, such as Django models, views, and forms. It helped me quickly scaffold CRUD functionality and suggested efficient ways to handle database queries. By iterating on its suggestions, I was able to refine my code and adopt more Pythonic practices.
  - Highlight: Copilot felt like a collaborative pair programmer, offering solutions to complex problems and teaching me new techniques. For example, it suggested optimized querysets for filtering volunteers based on user input, saving me time and effort.

- **Debugging:** 
  -Reflection: Debugging with Copilot was a learning experience. It not only identified errors but also provided insightful solutions that improved my understanding of Django’s framework. It encouraged me to simplify logic and write cleaner, more maintainable code.

- **Performance and UX Optimization:** 
  - Reflection: Copilot’s suggestions for front-end improvements, such as refining Bootstrap styling and improving responsiveness, elevated the platform’s design. Small changes, like aligning buttons and tweaking breakpoints, made the application feel polished and professional.



### Overall Impact:
Working with Copilot transformed my workflow. It allowed me to focus on higher-level decisions while handling repetitive tasks efficiently. However, it wasn’t always perfect—some suggestions required significant tweaking to fit my specific needs. Those moments were valuable reminders that the AI wasn’t a replacement for my skills but a tool to enhance them. 

Looking back, I feel this experience not only improved my technical abilities but also my problem-solving skills. It pushed me to articulate my ideas clearly (both to the AI and myself) and made me more mindful of inclusivity and accessibility in software design. Above all, it taught me the importance of embracing new technologies as partners in the creative process.

## GitHub Copilot
- **Code Creation:** 
  - Reflection: GitHub Copilot was instrumental in generating boilerplate code, such as Django models, views, and forms. It helped me quickly scaffold CRUD functionality and suggested efficient ways to handle database queries. By iterating on its suggestions, I was able to refine my code and adopt more Pythonic practices.
  - Highlight: Copilot felt like a collaborative pair programmer, offering solutions to complex problems and teaching me new techniques. For example, it suggested optimized querysets for filtering volunteers based on user input, saving me time and effort.

- **Debugging:** 
  -Reflection: Debugging with Copilot was a learning experience. It not only identified errors but also provided insightful solutions that improved my understanding of Django’s framework. It encouraged me to simplify logic and write cleaner, more maintainable code.

- **Performance and UX Optimization:** 
  - Reflection: Copilot’s suggestions for front-end improvements, such as refining Bootstrap styling and improving responsiveness, elevated the platform’s design. Small changes, like aligning buttons and tweaking breakpoints, made the application feel polished and professional.


# ChatGPT
### Problem-Solving and Guidance:
- Reflection: ChatGPT served as a mentor throughout the project, helping me understand complex concepts and providing detailed explanations for Django features. It was particularly helpful when I needed to implement advanced functionality, such as user-specific profiles and availability calendars.

- Highlight: ChatGPT’s ability to break down problems into manageable steps allowed me to approach challenges with confidence. For instance, it guided me through creating a separate profile model for referral users, ensuring the implementation was both efficient and scalable.

# Discord MidJourney
## Image Generation:
- Reflection: I used Discord MidJourney to generate custom images for the platform, such as placeholder profile pictures and visual assets for the landing page. These images added a professional and cohesive aesthetic to the application.
- Highlight: MidJourney’s AI-generated visuals enhanced the platform’s branding and user experience. The ability to create unique, high-quality images quickly was invaluable, especially for placeholders and decorative elements.

# Overall Impact
Using AI tools transformed my workflow and elevated the quality of the project. Each tool complemented the others, allowing me to focus on higher-level decisions while automating repetitive tasks and enhancing creativity. Here’s how these tools collectively impacted the project:
- Efficiency: Copilot and ChatGPT streamlined development by automating code generation and debugging, saving significant time.
- Creativity: MidJourney added a visual dimension to the project, ensuring the platform was both functional and visually appealing.
- Learning: Working with these tools deepened my understanding of Django, front-end design, and testing. They encouraged me to think critically about my code and design choices.
- Collaboration: The iterative nature of AI-assisted development felt like working with a team, where each tool brought its own expertise to the table.

While these tools were invaluable, they also reminded me of the importance of human oversight. Some suggestions required refinement to fit the project’s specific needs, reinforcing the idea that AI is a powerful assistant, not a replacement for human creativity and problem-solving.

## Documentation and Testing:
Reflection: ChatGPT assisted in writing clear and concise documentation, including README sections and testing summaries. It also helped me generate test cases for Django’s testing framework, ensuring comprehensive coverage of CRUD operations and user authentication.

## ------------------------------------------------------------------------------------------


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
- *Referral Users:
Add a feature to directly request help from a volunteer through the platform (e.g., a "Request Help" button).
Allow referral users to leave feedback or reviews for volunteers.

- Volunteers:
Add notifications for new requests from referral users.
Provide a dashboard to track their sessions and feedback.

- Shared Features:
Implement a messaging system for secure communication between referral users and volunteers.
Add a feature to schedule sessions directly within the platform.