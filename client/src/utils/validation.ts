export default function isEmpty(value: any) {
  return value?.toString().trim() === "";
}

export function isNotEqual(value: any, secondValue: any) {
  return value?.toString().trim() !== secondValue?.toString().trim();
}
