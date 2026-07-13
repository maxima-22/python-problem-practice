from FileReader import FileReader
from pathlib import Path


class ConfigManager:
    """
    Config Manager for AI Content Pipeline
    """

    # Class Attributes
    VALID_PROVIDERS = ["openai", "mistral", "deepseek"]
    REQUIRED_KEYS = ["api_key", "provider", "model"]
    MIN_KEY_LENGTH = 5

    def __init__(
        self,
        api_key: str,
        provider: str = "openai",
        model: str = "gpt-4o",
        temperature: float = 0.7,
        max_tokens: int = 4000,
    ) -> None:
        # Instead of self.__api_key = api_key we call @api_key.setter
        self.api_key = api_key
        self.provider = provider

        # Protected attributes
        self._model = model
        self._temperature = temperature
        self._max_tokens = max_tokens

    # =========== API Key =================

    # Masking self.api_key
    @property
    def api_key(self) -> str:
        """Returns masked API_key"""
        key = self.__api_key
        if len(key) > 10:
            return f"{key[:5]}...{key[-4:]}"
        return "****"

    @api_key.setter
    def api_key(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"API must be string, given: {type(value).__name__}")
        if len(value) < self.MIN_KEY_LENGTH:
            raise ValueError(f"Key is too short. Minimum length: {self.MIN_KEY_LENGTH}")
        self.__api_key = value

    # =========== Provider ===================

    @property
    def provider(self) -> str:
        return self._provider

    @provider.setter
    def provider(self, value: str) -> None:
        if value not in self.VALID_PROVIDERS:
            raise ValueError(
                f"Provider {value} is not supported. Valid providers: {', '.join(self.VALID_PROVIDERS)}"
            )
        self._provider = value

    # =========== Others ============

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def temperature(self) -> float:
        return self._temperature

    @property
    def max_tokens(self) -> int:
        return self._max_tokens

    # =======================================

    @property
    def is_configured(self) -> bool:
        """Checks if all data is correctly filled."""
        try:
            return (
                len(self.__api_key) >= self.MIN_KEY_LENGTH
                and self._provider in self.VALID_PROVIDERS
                and len(self._model) > 0
            )
        except AttributeError:
            return False

    @property
    def config_summary(self) -> dict:
        "Config summary"
        return {
            "api_key": self.api_key,
            "provider": self.provider,
            "model": self._model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "is_configured": self.is_configured,
        }

    # ========= Loading methods ===============

    def load_from_dict(self, data: dict) -> None:
        """
        Updates config from data.
        Updates only existant data.
        """
        if "api_key" in data:
            self.api_key = data["api_key"]
        if "provider" in data:
            self.provider = data["provider"]
        if "model" in data:
            self.model = data["model"]
        if "temperature" in data:
            self._temperature = float(data["temperature"])
        if "max_tokens" in data:
            self._max_tokens = int(data["max_tokens"])

    @classmethod
    def from_yaml(cls, path: str) -> "ConfigManager":
        """Create ConfigManager using FileReader"""
        reader = FileReader.from_yaml(path)
        config_data = reader.content

        missing = [key for key in cls.REQUIRED_KEYS if key not in config_data]
        if missing:
            raise KeyError(f"Config misses musthave values: {missing}")

        return cls(
            api_key=config_data["api_key"],
            provider=config_data.get("provider", "openai"),
            model=config_data.get("model", "gpt-4o"),
            temperature=config_data.get("temperature", 0.7),
            max_tokens=config_data.get("max_tokens", 4000),
        )

    # ========= Inner Methods ==============

    def _get_raw_key(self) -> str:
        """Hidden method for getting real API-key"""
        return self.__api_key

    def get_api_headers(self) -> dict:
        """
        Get headers for API
        Uses key inside. It doesnt show up.
        """
        key = self._get_raw_key()

        if self.provider == "openai":
            return {"Authorization": f"Bearer {key}"}
        elif self.provider == "mistral":
            return {"Authorization": f"Bearer {key}"}
        elif self.provider == "deepseek":
            return {"Authorization": f"Bearer {key}"}
        else:
            return {"Authorization": f"Bearer {key}"}


if __name__ == "__main__":
    print("=" * 70)
    print("CONFIG MANAGER — Full demonstration")
    print("=" * 70)

    # === Create config ===
    print("\nCreating config: ")
    config = ConfigManager(
        api_key="sk-proj-1234567890abcdefghijklmnopqrstuvwxyz",
        provider="openai",
        model="gpt-4o",
        temperature=0.7,
    )
    print(f"Конфигурация готова: {config.is_configured}")

    # Safe key print
    print(f"Безопасный вывод ключа: {config.api_key}")

    # Summary
    print(f"Summary: {config.config_summary}")

    # === Validation ===
    try:
        config.provider = "unknown"
    except ValueError as e:
        print(f"\nОшибка провайдера: {e}")

    try:
        config.api_key = "abc"
    except ValueError as e:
        print(f"Ошибка ключа: {e}")

    # === Changing configuration ===
    print("\n✏️ Changing configuration:")
    config.provider = "deepseek"
    config.model = "deepseek-chat"
    config.api_key = "sk-ds-9876543210zyxwvutsrqponmlkjihgfedcba"

    print(f"New summary: {config.config_summary}")

    # === Loading from dictionary ===
    print("\n📥 Loading from dictionary:")
    config.load_from_dict({"model": "claude-3-sonnet", "temperature": 0.5})
    print(f"After load_from_dict: model={config.model}, temp={config.temperature}")

    # === API-headers ===
    print("\nAPI-headers: ")
    headers = config.get_api_headers()
    # Masking for output
    safe_headers = {k: v[:20] + "..." if len(v) > 20 else v for k, v in headers.items()}
    print(f"Headers: {safe_headers}")

    # === Load from YAML ===
    print("\n📄 Loading from YAML:")
    config_path = Path(__file__).parent / "ai_pipeline.yaml"
    yaml_config = ConfigManager.from_yaml(str(config_path))
    print(f"From YAML: {yaml_config.config_summary}")

    print("\n" + "=" * 70)
    print("✅ ConfigManager ready for use in AI Content Pipeline!")
    print("=" * 70)
