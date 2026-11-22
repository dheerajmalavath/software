"""
Viva Question and Answer Data Store for Topic 2: Maven using Eclipse & CLI (50 questions).
"""

MAVEN_QUESTIONS = [
    (
        "What is Apache Maven?",
        "Apache Maven is an open-source build automation and project comprehension tool primarily used for Java projects. "
        "It standardizes project structures, automatically manages external dependencies via repositories, executes automated tests, "
        "and packages applications into distributable formats such as JAR or WAR files based on a central Project Object Model (pom.xml)."
    ),
    (
        "What are the key advantages of Maven over traditional build tools like Ant or manual JAR management?",
        "• Declarative Build: Configuration over coding; developers describe 'what' to build in XML rather than writing explicit imperative scripts.\n"
        "• Dependency Management: Automatically downloads transitive dependencies and caches them locally, preventing 'JAR hell'.\n"
        "• Standardized Project Layout: Every Maven project adheres to the exact same folder structure, making onboarding seamless.\n"
        "• Rich Plugin Ecosystem: Out-of-the-box integration for compilation, testing, packaging, code quality, and deployment."
    ),
    (
        "What is a POM (Project Object Model) and what is pom.xml?",
        "The Project Object Model (POM) is the core unit of configuration in Maven. "
        "'pom.xml' is the XML file in the root directory that contains all project configuration data, including GroupId, ArtifactId, Version (GAV), "
        "dependencies, build plugins, compile goals, profiles, and project metadata."
    ),
    (
        "What is GAV in Maven? Explain GroupId, ArtifactId, and Version.",
        "GAV uniquely identifies a Maven artifact worldwide across all repositories:\n"
        "• GroupId: Identifies the organization or domain creating the project (e.g. 'com.example' or 'org.apache.commons').\n"
        "• ArtifactId: The specific name of the project library or application (e.g. 'oltrs-app' or 'commons-lang3').\n"
        "• Version: The current release version (e.g. '1.0.0' for stable releases or '1.0-SNAPSHOT' for active development)."
    ),
    (
        "What are the standard Maven build lifecycles? (Clean, Default, Site)",
        "Maven provides three built-in build lifecycles:\n"
        "1. Clean Lifecycle: Handles project cleanup and artifact deletion (phases: pre-clean, clean, post-clean).\n"
        "2. Default (Build) Lifecycle: Handles code compilation, testing, packaging, and deployment (23 sequential phases).\n"
        "3. Site Lifecycle: Handles creation and deployment of project documentation and reports (phases: site, site-deploy)."
    ),
    (
        "What are the phases in the Maven default build lifecycle?",
        "The primary sequential phases in the default lifecycle are:\n"
        "1. validate: Validates project structure and required configuration information.\n"
        "2. compile: Compiles Java source code into bytecode (.class files).\n"
        "3. test: Runs unit tests (using JUnit/TestNG) without packaging.\n"
        "4. package: Packages compiled code into JAR or WAR format in the target/ folder.\n"
        "5. verify: Runs integration tests to ensure quality checks are met.\n"
        "6. install: Installs the package into local repository (~/.m2/repository).\n"
        "7. deploy: Copies final package to remote repository for sharing across teams."
    ),
    (
        "What is the difference between a Maven lifecycle, phase, and goal?",
        "• Lifecycle: A high-level sequence of steps (Clean, Default, Site).\n"
        "• Phase: A distinct stage within a lifecycle (e.g. 'compile', 'test', 'package'). Executing a phase automatically runs all preceding phases.\n"
        "• Goal: A specific executable task bound to a phase, provided by a plugin (e.g. 'compiler:compile' bound to compile phase, 'surefire:test' bound to test phase)."
    ),
    (
        "Explain the function of 'mvn clean'.",
        "'mvn clean' invokes the clean lifecycle, deleting the entire build output directory ('target/') on disk. "
        "This ensures that subsequent compilation runs are completely clean and do not use stale bytecode or outdated resources."
    ),
    (
        "Explain the function of 'mvn compile'.",
        "'mvn compile' runs validation, copies resources from 'src/main/resources' to 'target/classes', "
        "and invokes the 'maven-compiler-plugin' to compile all Java source files under 'src/main/java' into bytecode (.class files) inside 'target/classes/'."
    ),
    (
        "Explain the function of 'mvn test'.",
        "'mvn test' compiles the application source code, compiles test sources under 'src/test/java', "
        "and executes unit test cases using the Surefire plugin, outputting test execution reports and XML summaries into 'target/surefire-reports/'."
    ),
    (
        "Explain the function of 'mvn package'.",
        "'mvn package' compiles code, runs all unit tests, and packages the compiled classes and web resources into the distributable archive specified in pom.xml "
        "('<packaging>war</packaging>' or '<packaging>jar</packaging>') inside the 'target/' folder."
    ),
    (
        "Explain the function of 'mvn install'.",
        "'mvn install' executes all phases up to 'package' and then copies the resulting JAR or WAR artifact into the local Maven repository "
        "(on Ubuntu at '~/.m2/repository/<groupId>/<artifactId>/<version>/'). This makes the artifact immediately accessible as a dependency to other local Maven projects."
    ),
    (
        "Explain the function of 'mvn deploy'.",
        "'mvn deploy' is the final phase of the default lifecycle. It copies the finished build package to an external, shared remote repository "
        "(such as Nexus, Artifactory, or AWS CodeArtifact) to allow other team members and production servers to download it."
    ),
    (
        "What is the difference between 'mvn package' and 'mvn install'?",
        "'mvn package' only generates the archive (.jar/.war) locally inside the project's own 'target/' directory. "
        "'mvn install' generates the archive AND installs it into your user's global local repository cache ('~/.m2/repository'), "
        "making it available for other projects on your machine."
    ),
    (
        "What is the standard directory structure of a Maven project?",
        "• 'src/main/java': Production Java source files.\n"
        "• 'src/main/resources': Production properties and configuration files.\n"
        "• 'src/main/webapp': Web application resources (WEB-INF/web.xml, JSP, HTML, CSS).\n"
        "• 'src/test/java': Unit test classes.\n"
        "• 'src/test/resources': Test-specific configurations.\n"
        "• 'target/': Generated build output directory.\n"
        "• 'pom.xml': Maven configuration file in root directory."
    ),
    (
        "Why does Maven enforce a standard directory structure?",
        "Convention over Configuration. By enforcing a standard structure, any Java developer can open any Maven project and instantly know where "
        "source code, tests, and configuration files reside, eliminating the need to write custom build scripts specifying source directories."
    ),
    (
        "What is the purpose of 'src/main/resources'?",
        "It stores application configuration files (such as 'application.properties', 'log4j.properties', 'hibernate.cfg.xml', or database credentials). "
        "During compilation, Maven automatically copies all files from this directory directly into 'target/classes/', placing them at the root of the runtime classpath."
    ),
    (
        "What is the purpose of 'src/main/webapp' in web applications?",
        "In Maven web projects (with '<packaging>war</packaging>'), 'src/main/webapp' represents the root of the web archive. "
        "It contains static web assets (HTML, CSS, JS, JSP) and the protected 'WEB-INF/' folder containing 'web.xml' (Deployment Descriptor)."
    ),
    (
        "What is the local repository in Maven, and where is it located on Ubuntu?",
        "The local repository is a directory on the developer's computer where Maven stores and caches downloaded remote dependencies, plugins, and locally installed artifacts. "
        "On Ubuntu Linux, it is located at: '~/.m2/repository/'."
    ),
    (
        "What is the Maven Central Repository?",
        "Maven Central (repo.maven.apache.org) is the default public remote repository maintained by the Maven community. "
        "It contains hundreds of thousands of open-source Java libraries, dependencies, and plugins that Maven searches and downloads automatically."
    ),
    (
        "What is a Remote Repository in Maven?",
        "A remote repository is an external server (such as an internal corporate repository hosted on Nexus or Artifactory) configured in 'pom.xml' "
        "or 'settings.xml' to host private proprietary libraries and mirror public dependencies for faster team downloads."
    ),
    (
        "In what order does Maven search for dependencies?",
        "1. Local Repository ('~/.m2/repository'): Checks local cache first. If found, uses it immediately.\n"
        "2. Central Repository: If not in local cache, searches Maven Central.\n"
        "3. Remote Repositories: If defined in pom.xml, searches external enterprise repositories in listed order.\n"
        "Once downloaded, Maven caches the dependency in the local repository for future offline use."
    ),
    (
        "What is a Maven Archetype?",
        "An Archetype is a Maven project templating toolkit. It provides a standardized skeleton and generates pre-configured directory layouts "
        "and sample files for specific types of projects (such as standalone console applications, webapps, or Spring Boot services)."
    ),
    (
        "What is 'maven-archetype-quickstart', and what files does it generate?",
        "'maven-archetype-quickstart' generates a minimal standard Java application skeleton. "
        "It creates: (1) 'src/main/java/com/example/App.java' (containing main method printing Hello World), "
        "(2) 'src/test/java/com/example/AppTest.java' (sample JUnit test case), and (3) a basic 'pom.xml' with JUnit dependency."
    ),
    (
        "What is 'maven-archetype-webapp', and what files does it generate?",
        "'maven-archetype-webapp' generates a standard Java Web Application skeleton for deployment to servlet containers like Tomcat. "
        "It generates: (1) 'src/main/webapp/WEB-INF/web.xml', (2) 'src/main/webapp/index.jsp', and (3) 'pom.xml' with '<packaging>war</packaging>'."
    ),
    (
        "How do you create a Maven project in Eclipse IDE step-by-step?",
        "1. Open Eclipse → File → New → Other... → Maven → Maven Project → Click Next.\n"
        "2. Select workspace location → Click Next.\n"
        "3. Filter archetype by 'quickstart' or 'webapp' → Select 'maven-archetype-quickstart' → Click Next.\n"
        "4. Enter Group Id ('com.example'), Artifact Id ('my-app'), Version ('1.0-SNAPSHOT'), Package ('com.example').\n"
        "5. Click Finish. When prompted in Console with Y/N, type 'Y' and press Enter to generate project."
    ),
    (
        "How do you import an existing Maven project into Eclipse?",
        "1. Open Eclipse → File → Import...\n"
        "2. Expand 'Maven' folder → Select 'Existing Maven Projects' → Click Next.\n"
        "3. Click 'Browse...' and select the project root directory containing 'pom.xml'.\n"
        "4. Ensure checkbox for 'pom.xml' is checked → Click Finish. Eclipse automatically resolves dependencies."
    ),
    (
        "What does 'Maven -> Update Project' (Alt+F5) do in Eclipse?",
        "Right-clicking a project in Eclipse and selecting Maven → Update Project (Alt+F5) forces Eclipse to re-read 'pom.xml', "
        "re-synchronize dependencies, download missing JARs into the local cache, update the Java build path, and apply compiler plugin settings."
    ),
    (
        "How do you run Maven Clean, Install, and Test inside Eclipse UI?",
        "• Maven Clean: Right-click project or pom.xml → Run As → Maven Clean.\n"
        "• Maven Install: Right-click project or pom.xml → Run As → Maven Install.\n"
        "• Maven Test: Right-click project or pom.xml → Run As → Maven Test.\n"
        "Console output displays build logs and 'BUILD SUCCESS'."
    ),
    (
        "How do you configure custom Maven goals in Eclipse Run Configurations?",
        "1. Right-click project → Run As → Maven Build...\n"
        "2. In the Edit Configuration dialog, in the 'Goals' text box, type: 'clean install -DskipTests'.\n"
        "3. Click 'Apply' and click 'Run'. This configuration is saved under Run Configurations for one-click re-execution."
    ),
    (
        "What is a dependency in pom.xml?",
        "A dependency is an external library required by the project to compile, test, or execute. "
        "It is declared inside the '<dependencies>' tag using GroupId, ArtifactId, Version (GAV), and optional Scope."
    ),
    (
        "What is dependency scope in Maven? (compile, provided, runtime, test, system)",
        "• 'compile' (default): Available on all classpaths (compile, test, runtime) and packaged into final artifact.\n"
        "• 'provided': Required for compilation and test, but expected to be provided by JDK or container (e.g. Servlet API provided by Tomcat at runtime).\n"
        "• 'runtime': Needed for execution but not compilation (e.g. JDBC database drivers).\n"
        "• 'test': Only available during test compilation and test execution (e.g. JUnit, Mockito); not packaged into production JAR/WAR.\n"
        "• 'system': Similar to provided, but requires an explicit system path to a local JAR on disk."
    ),
    (
        "What is transitive dependency, and how does Maven resolve dependency conflicts?",
        "A transitive dependency occurs when Project A depends on Library B, and Library B depends on Library C. Maven automatically includes Library C on the classpath. "
        "If two libraries depend on conflicting versions of Library C, Maven resolves conflicts using the 'Nearest Definition' rule."
    ),
    (
        "What is the 'nearest definition' rule in Maven dependency mediation?",
        "Maven chooses the dependency version that is closest to your project in the dependency tree. "
        "If Project A -> B -> C (v1.0) and Project A -> D -> E -> C (v2.0), Maven selects C v1.0 because it is 2 levels deep, whereas C v2.0 is 3 levels deep."
    ),
    (
        "What is dependency exclusion (<exclusions>), and when is it needed?",
        "An exclusion tag ('<exclusions>') inside a '<dependency>' tells Maven NOT to pull in a specific transitive dependency. "
        "It is needed when a transitive dependency has a known security vulnerability, causes a classpath collision, or conflicts with a newer version explicitly declared."
    ),
    (
        "What is a Maven Plugin, and how does it differ from a dependency?",
        "A dependency is a library containing classes that your application source code calls at runtime. "
        "A plugin is an executable extension to Maven itself that performs actions during the build process (e.g. compiling Java files, creating WAR files, executing tests, or generating reports)."
    ),
    (
        "What is the role of maven-compiler-plugin?",
        "The 'maven-compiler-plugin' compiles the Java source code of the project. "
        "It allows configuring the source and target Java bytecode compatibility versions (e.g. Java 17) and passing compiler arguments to the javac compiler."
    ),
    (
        "How do you configure the Java version (e.g. Java 17) in maven-compiler-plugin?",
        "In 'pom.xml' inside '<build><plugins>':\n"
        "<plugin>\n"
        "  <groupId>org.apache.maven.plugins</groupId>\n"
        "  <artifactId>maven-compiler-plugin</artifactId>\n"
        "  <version>3.11.0</version>\n"
        "  <configuration>\n"
        "    <source>17</source>\n"
        "    <target>17</target>\n"
        "  </configuration>\n"
        "</plugin>"
    ),
    (
        "What is maven-surefire-plugin?",
        "The Surefire plugin executes unit tests during the 'test' phase of the build lifecycle. "
        "It automatically finds and runs test classes matching '**/*Test.java', '**/Test*.java', or '**/*TestCase.java', generating test reports in TXT and XML formats."
    ),
    (
        "What is maven-war-plugin?",
        "The WAR plugin packages web applications into Web Application Archive (.war) files. "
        "It bundles compiled classes from 'target/classes/', web assets from 'src/main/webapp/', and external dependencies into 'WEB-INF/lib/'."
    ),
    (
        "What is maven-jar-plugin, and how do you configure the main class in the manifest?",
        "The JAR plugin builds standard Java Archive (.jar) files. To make the JAR directly executable via 'java -jar app.jar', configure the main class in the manifest:\n"
        "<configuration>\n"
        "  <archive>\n"
        "    <manifest>\n"
        "      <mainClass>com.example.App</mainClass>\n"
        "    </manifest>\n"
        "  </archive>\n"
        "</configuration>"
    ),
    (
        "How do you skip test execution during a Maven build in Ubuntu terminal?",
        "Execute either of the following commands:\n"
        "$ mvn clean package -DskipTests\n"
        "(Compiles tests but skips execution).\n"
        "$ mvn clean package -Dmaven.test.skip=true\n"
        "(Skips both test compilation and test execution)."
    ),
    (
        "How do you run only a specific test class or test method using Maven CLI?",
        "Use the '-Dtest' parameter:\n"
        "• Single test class: $ mvn test -Dtest=AppTest\n"
        "• Specific test method: $ mvn test -Dtest=AppTest#testLoginSuccess\n"
        "• Wildcard pattern: $ mvn test -Dtest=*ValidationTest"
    ),
    (
        "How do you troubleshoot Maven build failures using debug mode? (The -X switch)",
        "Run the build command appending the '-X' switch:\n"
        "$ mvn clean package -X\n"
        "This enables full verbose debug output, printing classpaths, detailed stack traces, exact URLs checked during dependency resolution, and plugin execution internals."
    ),
    (
        "What causes the 'Unsupported class version error' in Maven, and how do you fix it?",
        "Cause: The Java bytecode was compiled targeting a newer Java version (e.g. Java 17 = version 61.0) than the Java Runtime Environment (JRE) running the application (e.g. Java 11 = version 55.0).\n"
        "Fix: Align the compiler plugin '<source>' and '<target>' in pom.xml to match the installed runtime JRE, or upgrade the runtime Java version on Ubuntu using 'sudo update-alternatives --config java'."
    ),
    (
        "What causes 'Failed to execute goal maven-compiler-plugin:compile', and how do you resolve it?",
        "Common Causes: (1) Java syntax errors in source code, (2) missing imported classes/dependencies in pom.xml, or (3) JDK version mismatch.\n"
        "Resolution: Check the console error line number, fix source code syntax or typo in pom.xml dependency tags, run with '-X' for stack trace, and execute 'mvn clean compile'."
    ),
    (
        "How do you change the default build output directory from target/ to build_output/ in pom.xml?",
        "In 'pom.xml', specify the '<directory>' tag inside '<build>':\n"
        "<build>\n"
        "  <directory>${project.basedir}/build_output</directory>\n"
        "</build>\n"
        "After running 'mvn compile', binaries will be written to 'build_output/' instead of 'target/'."
    ),
    (
        "What is a multi-module Maven project, and what is a parent POM?",
        "A multi-module project organizes a complex system into smaller interdependent sub-projects (e.g. core, service, web). "
        "The root directory contains a Parent POM with '<packaging>pom</packaging>' that declares submodules in '<modules><module>core</module>...</modules>', "
        "allowing the entire suite of modules to be built in correct dependency order with a single command."
    ),
    (
        "What is the purpose of <dependencyManagement> vs <dependencies> in parent POMs?",
        "• '<dependencies>': Dependencies declared here are unconditionally inherited by all child submodules.\n"
        "• '<dependencyManagement>': Acts as a centralized dictionary defining dependency versions and configurations without actually adding them to classpaths. "
        "Child modules declare dependencies without specifying '<version>', ensuring uniform versions across the entire enterprise project."
    ),
    (
        "How do you generate a test coverage and project site documentation report in Maven?",
        "Run: $ mvn site\n"
        "This compiles project reports, Javadoc, Surefire test reports, and dependency analysis into HTML web documentation located inside 'target/site/index.html'."
    )
]

print(f"Maven questions compiled: {len(MAVEN_QUESTIONS)}")
