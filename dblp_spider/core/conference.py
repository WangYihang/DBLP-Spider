import termcolor


class Conference:
    def __init__(self, name, venue, short, keywords) -> None:
        self.name = name
        self.venue = venue
        self.short = short
        self.keywords = keywords

    def __str__(self):
        if len(self.keywords) > 0:
            ccf_class = self.keywords[0]
            if ccf_class.endswith("A"):
                return "{} - {} ({})".format(termcolor.colored(self.keywords[0], "green"), self.name, self.short)
            elif ccf_class.endswith("B"):
                return "{} - {} ({})".format(termcolor.colored(self.keywords[0], "yellow"), self.name, self.short)
            elif ccf_class.endswith("C"):
                return "{} - {} ({})".format(termcolor.colored(self.keywords[0], "magenta"), self.name, self.short)
            else:
                return "{} - {} ({})".format(self.keywords[0], self.name, self.short)
        else:
            return "{} ({})".format(self.name, self.short)


Conferences = set()

# Cyber Security CCF A
Conferences_CCF_A = set()
Conferences_CCF_A.add(Conference(name="ACM Conferenceon Computer and Communications Security",
                                 venue="CCS", short="CCS", keywords=["CCF - A"]))
Conferences_CCF_A.add(Conference(name="International Cryptology Conference",
                                 venue="CRYPTO", short="CRYPTO", keywords=["CCF - A"]))
Conferences_CCF_A.add(Conference(name="European Cryptology Conference",
                                 venue="EUROCRYPT", short="EUROCRYPT", keywords=["CCF - A"]))
Conferences_CCF_A.add(Conference(name="IEEE Symposium on Security and Privacy",
                                 venue="IEEE_Symposium_on_Security_and_Privacy_Workshops", short="S&P", keywords=["CCF - A"]))
Conferences_CCF_A.add(Conference(name="Usenix Security Symposium",
                                 venue="USENIX_Security_Symposium", short="USENIX", keywords=["CCF - A"]))

# Cyber Security CCF B
Conferences_CCF_B = set()
Conferences_CCF_B.add(Conference(name="Annual Computer Security Applications Conference",
                                 venue="ACSAC", short="ACSAC", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="Annual International Conference on the Theory and Application of Cryptology and Information Security",
                                 venue="ASIACRYPT", short="ASIACRYPT", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="Conference on Cryptographic Hardware and Embedded Systems",
                                 venue="CHES", short="CHES", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="IEEE Computer Security Foundations Symposium",
                                 venue="CSF", short="CSF", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="International Conference on Dependable Systems and Networks",
                                 venue="DSN", short="DSN", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="European Symposiumon Research in Computer Security",
                                 venue="ESORICS", short="ESORICS", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="Fast Software Encryption",
                                 venue="FSE", short="FSE", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="Network and Distributed System Security Symposium",
                                 venue="NDSS", short="NDSS", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="International Workshop on Practice and Theory in Public Key Cryptography",
                                 venue="PKC", short="PKC", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="International Symposium on Research in Attacks, Intrusions, and Defenses",
                                 venue="RAID", short="RAID", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="IEEE International Symposium on Reliable Distributed Systems",
                                 venue="SRDS", short="SRDS", keywords=["CCF - B"]))
Conferences_CCF_B.add(Conference(name="Theory of Cryptography Conference",
                                 venue="TCC", short="TCC", keywords=["CCF - B"]))

# Cyber Security CCF C
Conferences_CCF_C = set()
Conferences_CCF_C.add(Conference(name="Australasia Conference on Information Security and Privacy",
                                 venue="ACISP", short="ACISP", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="International Conference on Applied Cryptography and Network Security",
                                 venue="ACNS", short="ACNS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="ACM Asia Conference on Computer and Communications Security",
                                 venue="ASIACCS", short="ASIACCS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="EAI International Conference on Cyber Attacks Response and Defense",
                                 venue="CARDS", short="CARDS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="RSA Conference, Cryptographers' Track",
                                 venue="CT-RSA", short="RSA", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Digital Forensic Research Workshop",
                                 venue="DFRWS-EU", short="EU", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Digital Forensic Research Workshop",
                                 venue="DFRWS-USA", short="USA", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Detection of Intrusions and Malware & Vulnerability Assessment",
                                 venue="DIMVA", short="DIMVA", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Financial Cryptography and Data Security",
                                 venue="FC", short="FC", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="USENIX Workshop on Hot Topics in Security",
                                 venue="HotSec", short="HotSec", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="International Conference on Information and Communications Security",
                                 venue="ICICS", short="ICICS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="IFIP WG 11.9 International Conference on Digital Forensics",
                                 venue="IFIP WG 11.9", short="9", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="ACM Workshop on Information Hiding and Multimedia Security",
                                 venue="IH&MMSec", short="MMSec", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Information Security Conference",
                                 venue="ISC", short="ISC", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="New Security Paradigms Workshop",
                                 venue="NSPW", short="NSPW", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Passive and Active Measurement Conference",
                                 venue="PAM", short="PAM", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Privacy Enhancing Technologies Symposium",
                                 venue="PETS", short="PETS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Selected Areas in Cryptography",
                                 venue="SAC", short="SAC", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="ACM Symposium on Access Control Models and Technologies",
                                 venue="SACMAT", short="SACMAT", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="IFIP International Information Security and Privacy Conference",
                                 venue="SEC", short="SEC", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="Symposium On Usable Privacy and Security",
                                 venue="SOUPS", short="SOUPS", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="International Conference on Security and Privacy in Communication Networks",
                                 venue="SecureComm", short="SecureComm", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="IEEE International Conference on Trust, Security and Privacy in Computing and Communications",
                                 venue="TrustCom", short="TrustCom", keywords=["CCF - C"]))
Conferences_CCF_C.add(Conference(name="ACM Conference on Security and Privacy in Wireless and Mobile Networks",
                                 venue="WISEc", short="WISEc", keywords=["CCF - C"]))

# Network CCF A
Conferences_CCF_A.add(Conference(name="IEEE International Conference on Computer Communications",
                                 venue="INFOCOM", short="INFOCOM", keywords=["CCF - A"]))
Conferences_CCF_A.add(Conference(name="ACM Special Interest Group on Data Communication",
                                 venue="SIGCOMM", short="SIGCOMM", keywords=["CCF - A"]))

Conferences_CCF_B.add(Conference(
    name="ACM Internet Measurement Conference", venue="Internet_Measurement_Conference", short="IMC", keywords=["CCF - B"]))

# Not in CCF Recommendations
Conferences.add(Conference(
    name="Computing Research Repository", venue="CoRR", short="CoRR", keywords=[]))
Conferences.add(Conference(name="IEEE Access",
                           venue="IEEE_Access", short="ACCESS", keywords=[]))
Conferences.add(Conference(name="IEEE European Symposium on Security and Privacy",
                           venue="EuroS&P", short="EuroS&P", keywords=["CCF - A"]))
Conferences.add(Conference(
    name="IEEE International Conference on Communications", venue="ICC", short="ICC", keywords=[]))

Conferences = Conferences.union(Conferences_CCF_A)
Conferences = Conferences.union(Conferences_CCF_B)
Conferences = Conferences.union(Conferences_CCF_C)
