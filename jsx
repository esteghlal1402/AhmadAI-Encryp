export default function InputBox({ value, onChange }) {
  return (
    <textarea
      className="w-full p-4 rounded-lg border mb-4"
      placeholder="یه سایت فروشگاهی می‌خوام..."
      value={value}
      onChange={onChange}
    />
  );
}
