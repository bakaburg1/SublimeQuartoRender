import sublime
import sublime_plugin
import subprocess
import os

class QuartoRenderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get the current file path
        file_path = self.view.file_name()
        
        if not file_path:
            sublime.error_message("Please save the file before rendering.")
            return
        
        if not file_path.endswith('.qmd'):
            sublime.error_message("This is not a Quarto document (.qmd file)")
            return
        
        # Get the directory of the current file
        file_dir = os.path.dirname(file_path)
        
        # Show a status message
        sublime.status_message("Rendering Quarto document...")
        
        # Run the quarto render command
        try:
            result = subprocess.run(['quarto', 'render', file_path], 
                                    cwd=file_dir, 
                                    capture_output=True, 
                                    text=True)
            
            if result.returncode == 0:
                sublime.status_message("Quarto document rendered successfully")
            else:
                sublime.error_message(f"Error rendering Quarto document: {result.stderr}")
        except FileNotFoundError:
            sublime.error_message("Quarto CLI not found. Make sure it's installed and in your PATH.")