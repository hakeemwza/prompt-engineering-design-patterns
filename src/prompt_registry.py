from dataclasses import dataclass

@dataclass
class PromptPattern:
    name: str
    description: str
    use_case: str


PATTERNS = [
    PromptPattern(
        name="Zero-Shot Prompting",
        description="Completes a task without examples.",
        use_case="Simple classification and summarization"
    ),
    PromptPattern(
        name="Few-Shot Prompting",
        description="Improves consistency by providing examples.",
        use_case="Information extraction and structured outputs"
    ),
    PromptPattern(
        name="Role Prompting",
        description="Assigns expertise or context to the model.",
        use_case="Domain-specific reasoning"
    )
]

if __name__ == "__main__":
    for pattern in PATTERNS:
        print(f"{pattern.name}: {pattern.use_case}")