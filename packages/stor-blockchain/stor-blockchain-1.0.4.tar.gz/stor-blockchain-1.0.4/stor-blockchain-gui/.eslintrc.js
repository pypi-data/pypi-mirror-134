module.exports = {
  extends: [
    "airbnb-typescript",
    "airbnb/hooks",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "plugin:eslint-comments/recommended",
    "plugin:promise/recommended",
    "plugin:unicorn/recommended",
    "prettier",
  ],
  plugins: [
    "@typescript-eslint",
    "eslint-comments",
    "promise",
    "unicorn",
    "react",
    "jsx-a11y",
    "import",
    "prettier",
  ],
  env: {
    "browser": true,
    "es6": true,
    "jest": true,
  },
  parser: "@typescript-eslint/parser",
  parserOptions: {
    sourceType: "module",
    project: "./tsconfig.json",
    ecmaFeatures: {
      jsx: true,
    },
  },
  rules: {
    "jsx-a11y/anchor-is-valid": "off",
    "consistent-return": "off",
    "react/no-danger": "off",
    "no-case-declarations": "off",
    "eslint-comments/no-unlimited-disable": "off",
    "@typescript-eslint/naming-convention": "off",
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/await-thenable": "off",
    "@typescript-eslint/no-unsafe-member-access": "off",
    "@typescript-eslint/no-unsafe-assignment": "off",
    "@typescript-eslint/ban-ts-comment": "off",
    "@typescript-eslint/no-unsafe-call": "off",
    "@typescript-eslint/restrict-template-expressions": "off",
    "@typescript-eslint/ban-types": "off",
    "@typescript-eslint/no-shadow": "off",
    "@typescript-eslint/no-unsafe-return": "off",
    "@typescript-eslint/restrict-plus-operands": "off",
    "@typescript-eslint/unbound-method": "off",
    "@typescript-eslint/explicit-module-boundary-types": "off",
    "@typescript-eslint/no-floating-promises": "off",
    "react/jsx-props-no-spreading": "off",
    "react/destructuring-assignment": "off",
    "react/require-default-props": "off",
    "react/default-props-match-prop-types": "off",
    "unicorn/no-abusive-eslint-disable": "off",
    "unicorn/no-nested-ternary": "off",
    "unicorn/no-object-as-default-parameter": "off",
    "unicorn/explicit-length-check": "off",
    "unicorn/no-null": "off",
    "unicorn/no-reduce": "off",
    "unicorn/consistent-function-scoping": "off",
    "unicorn/prevent-abbreviations": "off",
    "unicorn/no-lonely-if": "off",
    "unicorn/no-array-reduce": "off",
    "unicorn/no-new-array": "off",
    "unicorn/no-array-for-each": "off",
    "unicorn/prefer-spread": "off",
    "unicorn/consistent-destructuring": "off",
    "unicorn/filename-case": ["error", {
      "cases": {
        "camelCase": true,
        "pascalCase": true,
      },
    }],
  },
};
