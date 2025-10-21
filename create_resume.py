from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Prateek Punetha", ln=True, align="C")
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Analyst Trainee", ln=True, align="C")
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

# --- Create PDF ---
pdf = ResumePDF()
pdf.set_margins(left=10, top=10, right=10)
pdf.add_page()

# --- Summary ---
pdf.section_title("Summary")
pdf.section_body(
    "Analyst Trainee at Cognizant with a passion for Linux system administration, cloud infrastructure, and DevOps automation. "
    "Hands-on with system support, troubleshooting, and process optimization in enterprise environments. "
    "Eager to expand expertise in cloud operations, scripting, and CI/CD automation."
)

# --- Skills ---
pdf.section_title("Skills")
pdf.skill_line("Cloud Platforms:", "AWS (EC2, S3, IAM), basic Azure/GCP")
pdf.skill_line("Operating Systems:", "Linux administration and troubleshooting")
pdf.skill_line("DevOps Tools:", "Git, Docker, NGINX, CI/CD basics")
pdf.skill_line("Scripting:", "Bash, Python")
pdf.skill_line("Networking:", "TCP/IP, DNS, firewall")
pdf.skill_line("Soft Skills:", "Communication, Problem Solving, Adaptability")

# --- Experience ---
pdf.section_title("Experience")
pdf.section_body(
    "Analyst Trainee — Cognizant (Aug 2025 – Present)\n"
    "• Supporting enterprise IT environments through incident resolution, patching, and service operations.\n"
    "• Collaborating with cross-functional teams to ensure uptime, access control, and system reliability.\n"
    "• Exposure to automation, monitoring tools, and DevOps workflows within large-scale infrastructure."
)

# --- Projects ---
pdf.section_title("Projects")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "SysUI", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Python-based GUI for Linux sysadmins to simplify administration and implement security hardening measures.")
pdf.add_link_line("https://github.com/prateekpunetha/SysUI", "https://github.com/prateekpunetha/SysUI")

pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "termux-setup", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Bash automation script for quick environment setup on Termux.")
pdf.add_link_line("https://github.com/prateekpunetha/termux-setup", "https://github.com/prateekpunetha/termux-setup")

pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "bdaynotifier", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.section_body("Telegram bot built with Playwright to send automated birthday notifications.")
pdf.add_link_line("https://github.com/prateekpunetha/bdaynotifier", "https://github.com/prateekpunetha/bdaynotifier")

# --- Education ---
pdf.section_title("Education")
pdf.section_body(
    "Masters of Computer Applications (MCA), 2023–2025 — Pune University\n"
    "Bachelor of Science in Computer Science, 2019–2023 — Shivaji University"
)

# --- Save ---
pdf.output("resume.pdf")
