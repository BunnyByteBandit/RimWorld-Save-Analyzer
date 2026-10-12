import os
import xml.etree.ElementTree as ET

class RimWorldSaveAnalyzer:
    """
    A tool to inspect RimWorld .rws save files and extract metadata.
    """
    def __init__(self, save_path):
        self.save_path = save_path

    def parse_save(self):
        if not os.path.exists(self.save_path):
            return f"[!] Error: Save file '{self.save_path}' not found."
        
        try:
            tree = ET.parse(self.save_path)
            root = tree.getroot()
            
            game_version = root.findtext(".//meta/gameVersion", "Unknown")
            mod_list = [mod.text for mod in root.findall(".//meta/modIds/li")]
            
            return {
                "version": game_version,
                "total_mods": len(mod_list),
                "mods": mod_list
            }
        except Exception as e:
            return f"[!] Parsing error: {str(e)}"

if __name__ == "__main__":
    print("=== RimWorld Mod & Save Analyzer CLI ===")
    print("[+] Status: Ready for save file inspection.")
