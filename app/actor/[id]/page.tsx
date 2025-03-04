const Actor = async ({ params }: { params: Promise<{ id: number }> }) => {
  const { id } = await params;
  return (<div></div>);
};

export default Actor;
