from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Prateek Punetha", ln=True, align="C")
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Cloud Support Engineer | Linux System Administrator", ln=True, align="C")
        self.set_font("Helvetica", "", 9)
        self.cell(0, 6, "Pune, India | hi@prateekpunetha.dev | prateekpunetha.dev | github.com/prateekpunetha", ln=True, align="C")
        self.cell(0, 6, "linkedin.com/in/prateekpunetha", ln=True, align="C")
        self.ln(10)

    def draw_horizontal_line(self):
        self.set_draw_color(150, 150, 150)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(10, y, 200, y)
        self.ln(3)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(40, 40, 40)
        self.cell(0, 8, title, ln=True)
        self.set_text_color(0, 0, 0)
        self.draw_horizontal_line()

    def section_body(self, text):
        self.set_font("Helvetica", "", 10)
        text = text.encode("ascii", "ignore").decode()
        self.multi_cell(0, 5, text)
        self.ln(1)

    def add_link_line(self, title, url):
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(0, 0, 255)
        title = title.encode("ascii", "ignore").decode()
        self.cell(0, 6, title, ln=True, link=url)
        self.set_text_color(0, 0, 0)

    def skill_line(self, label, value):
        self.set_font("Helvetica", "B", 10)
        self.write(5, label)
        self.set_font("Helvetica", "", 10)
        self.write(5, f" {value}\n")

# create pdf
pdf = ResumePDF()
pdf.set_margins(left=10, top=10, right=10)
pdf.add_page()

pdf.section_title("Summary")
pdf.section_body(
    "Self-taught Linux System Administrator and aspiring Cloud Support Engineer with hands-on experience in Linux troubleshooting, AWS services, and scripting. "
    "Strong problem-solving skills and clear communication ability. Built and deployed projects involving cloud configuration, automation, and customer support simulation."
)

pdf.section_title("Skills")
pdf.skill_line("Cloud Platforms:", "AWS (EC2, S3, IAM), basic Azure/GCP")
pdf.skill_line("Operating Systems:", "Linux administration and troubleshooting")
pdf.skill_line("Networking:", "TCP/IP, DNS, firewall")
pdf.skill_line("Scripting:", "Bash, Python")
pdf.skill_line("Tools:", "Git, Docker, NGINX, Vim")
pdf.skill_line("Soft Skills:", "Communication, Customer Support, Problem Solving, Adaptability")

pdf.section_title("Certifications")
pdf.section_body(
    "- Introduction to Linux (LFS101) - Linux Foundation"
)

pdf.section_title("Education")
pdf.section_body(
    "Masters of Computer Applications (MCA), Computer Applications, 2023-2025\n"
    "Institute of Industrial Computer Management Research (Pune University)\n"
    "CGPA: 8.30/10\n\n"
    "Bachelor of Science, Computer Science, 2019-2023\n"
    "Vivekanand College (Shivaji University)\n"
    "CGPA: 8.96/10"
)

pdf.section_title("Cloud Experience")
pdf.section_body(
    "* Launched and managed EC2 instances, S3 buckets, IAM roles and policies on AWS\n"
    "* Simulated customer problems like SSH failures, S3 permission errors, broken nginx setups, and solved them\n"
    "* Practiced troubleshooting and escalation workflows similar to actual support environments"
)

pdf.section_title("Projects")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "SysUI", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Python-based GUI for Linux sysadmins to simplify process of administrating and implement security hardening measures.")
pdf.add_link_line("https://github.com/prateekpunetha/SysUI", "https://github.com/prateekpunetha/SysUI")

pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "termux-setup", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Bash automation for Termux setup.")
pdf.add_link_line("https://github.com/prateekpunetha/termux-setup", "https://github.com/prateekpunetha/termux-setup")

pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "bdaynotifier", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Telegram bot written in Playwright to announce birthdays.")
pdf.add_link_line("https://github.com/prateekpunetha/bdaynotifier", "https://github.com/prateekpunetha/bdaynotifier")

pdf.output("resume.pdf")
