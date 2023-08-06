	.file	"export_perf_count_macros.cpp"
	.text
	.section	.rodata
	.type	_ZStL19piecewise_construct, @object
	.size	_ZStL19piecewise_construct, 1
_ZStL19piecewise_construct:
	.zero	1
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.align 8
.LC0:
	.string	"from .PerformanceCounterSpec import PerformanceCounterSpec\n"
	.align 8
.LC1:
	.string	"# Generated with export_perf_count_macros.  Don't edit\n"
.LC2:
	.string	"PERF_TYPE_HARDWARE= "
.LC3:
	.string	"\n"
.LC4:
	.string	"PERF_TYPE_HW_CACHE= "
.LC5:
	.string	"PERF_TYPE_SOFTWARE= "
.LC6:
	.string	"CPU_CYCLES"
.LC7:
	.string	" = PerformanceCounterSpec("
.LC8:
	.string	", "
.LC9:
	.string	")\n"
.LC10:
	.string	"INSTRUCTIONS"
.LC11:
	.string	"CACHE_REFERENCES"
.LC12:
	.string	"CACHE_MISSES"
.LC13:
	.string	"BRANCH_INSTRUCTIONS"
.LC14:
	.string	"BRANCH_MISSES"
.LC15:
	.string	"BUS_CYCLES"
.LC16:
	.string	"STALLED_CYCLES_FRONTEND"
.LC17:
	.string	"STALLED_CYCLES_BACKEND"
.LC18:
	.string	"REF_CPU_CYCLES"
.LC19:
	.string	"CPU_CLOCK"
.LC20:
	.string	"TASK_CLOCK"
.LC21:
	.string	"PAGE_FAULTS"
.LC22:
	.string	"CONTEXT_SWITCHES"
.LC23:
	.string	"CPU_MIGRATIONS"
.LC24:
	.string	"PAGE_FAULTS_MIN"
.LC25:
	.string	"PAGE_FAULTS_MAJ"
.LC26:
	.string	"ALIGNMENT_FAULTS"
.LC27:
	.string	"EMULATION_FAULTS"
.LC28:
	.string	"DUMMY"
.LC29:
	.string	"L1D"
.LC30:
	.string	" = "
.LC31:
	.string	"L1I"
.LC32:
	.string	"LL"
.LC33:
	.string	"DTLB"
.LC34:
	.string	"ITLB"
.LC35:
	.string	"BPU"
.LC36:
	.string	"NODE"
.LC37:
	.string	"READ"
.LC38:
	.string	"WRITE"
.LC39:
	.string	"PREFETCH"
.LC40:
	.string	"ACCESS"
.LC41:
	.string	"MISS"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1498:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC0(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC1(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC2(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC4(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$3, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC5(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC6(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC10(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC11(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$2, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC12(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$3, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC13(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$4, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC14(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$5, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC15(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$6, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC16(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$7, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC17(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$8, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC18(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$9, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC19(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC20(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC21(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$2, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC22(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$3, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC23(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$4, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC24(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$5, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC25(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$6, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC26(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$7, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC27(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$8, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC28(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC7(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC8(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$9, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC9(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC29(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC31(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC32(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$2, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC33(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$3, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC34(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$4, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC35(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$5, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC36(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$6, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC37(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC38(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC39(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$2, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC40(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC41(%rip), %rsi
	movq	_ZSt4cout@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	leaq	.LC30(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$1, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi@PLT
	leaq	.LC3(%rip), %rsi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1498:
	.size	main, .-main
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1818:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	cmpl	$1, -4(%rbp)
	jne	.L5
	cmpl	$65535, -8(%rbp)
	jne	.L5
	leaq	_ZStL8__ioinit(%rip), %rdi
	call	_ZNSt8ios_base4InitC1Ev@PLT
	leaq	__dso_handle(%rip), %rdx
	leaq	_ZStL8__ioinit(%rip), %rsi
	movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rax
	movq	%rax, %rdi
	call	__cxa_atexit@PLT
.L5:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1818:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_export_perf_count_macros.cpp, @function
_GLOBAL__sub_I_export_perf_count_macros.cpp:
.LFB1819:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1819:
	.size	_GLOBAL__sub_I_export_perf_count_macros.cpp, .-_GLOBAL__sub_I_export_perf_count_macros.cpp
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I_export_perf_count_macros.cpp
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
