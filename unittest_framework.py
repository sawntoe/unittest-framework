from rich.console import Console

class UnitTest:
    def __init__(self) -> None:
        self.registry = []
        self.nofail_registry = []
        self.console = Console()
    
    def register(self, func):
        self.registry.append(func)
        return func
    
    def register_nofail(self, func):
        self.nofail_registry.append(func)
        return func
    def run(self):
        for i in range(len(self.registry)):
            test = self.registry[i]
            status = self.console.status(f"Executing test {i+1}...", spinner="dots")
            status.start()
            try:
                assert test() != False
                status.stop()
                self.console.print(f"[bold white]Executing test {i+1}...[bold green]OK")
            except BaseException as e:
                status.stop()
                self.console.print(f"[bold white]Executing test {i+1}...[bold red]FAIL")
                self.console.print_exception()
                exit(1)
        
        nofail_pass_count = 0
        for i in range(len(self.nofail_registry)):
            test = self.nofail_registry[i]
            status = self.console.status(f"Executing nofail test {i+1}...", spinner="dots")
            status.start()
            try:
                assert test() != False
                status.stop()
                self.console.print(f"[bold white]Executing nofail test {i+1}...[bold green]OK")
                nofail_pass_count += 1
            except BaseException as e:
                status.stop()
                self.console.print(f"[bold white]Executing nofail test {i+1}...[bold red]FAIL")
                self.console.print_exception()
        
        if nofail_pass_count == len(self.nofail_registry):
            self.console.print("[bold green]ALL TESTS PASSED")
        else:
            self.console.print("[bold red]SOME TESTS FAILED!")
             
             
